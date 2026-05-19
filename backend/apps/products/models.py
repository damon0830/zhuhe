import uuid
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("名称", max_length=100)
    name_en = models.CharField("英文名", max_length=100, blank=True)
    slug = models.SlugField("Slug", unique=True, max_length=120)
    description = models.TextField("描述", blank=True)
    image = models.ImageField("分类图", upload_to="categories/", blank=True)
    sort_order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("启用", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "产品分类"
        verbose_name_plural = "产品分类"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en or self.name)
        super().save(*args, **kwargs)


class Collection(models.Model):
    name = models.CharField("系列名称", max_length=100)
    slug = models.SlugField("Slug", unique=True, max_length=120)
    description = models.TextField("描述", blank=True)
    subtitle = models.CharField("副标题", max_length=200, blank=True)
    image = models.ImageField("系列图", upload_to="collections/", blank=True)
    bg_gradient = models.CharField("渐变背景", max_length=100, blank=True,
                                   help_text="Tailwind gradient classes")
    is_featured = models.BooleanField("首页展示", default=False)
    sort_order = models.PositiveIntegerField("排序", default=0)
    is_active = models.BooleanField("启用", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "系列"
        verbose_name_plural = "系列"
        ordering = ["sort_order"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    PEARL_TYPES = [
        ("akoya", "Akoya"),
        ("south_sea", "South Sea"),
        ("freshwater", "Freshwater"),
        ("tahitian", "Tahitian"),
        ("golden", "Golden South Sea"),
        ("baroque", "Baroque"),
        ("other", "Other"),
    ]

    name = models.CharField("产品名称", max_length=200)
    name_en = models.CharField("英文名", max_length=200, blank=True)
    slug = models.SlugField("Slug", unique=True, max_length=200)
    sku_prefix = models.CharField("SKU前缀", max_length=20, blank=True)
    description = models.TextField("描述", blank=True)
    short_description = models.CharField("简短描述", max_length=300, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="分类", related_name="products"
    )
    collections = models.ManyToManyField(
        Collection, blank=True, verbose_name="所属系列", related_name="products"
    )

    pearl_type = models.CharField("珍珠类型", max_length=20, choices=PEARL_TYPES, default="akoya")
    pearl_size = models.CharField("珍珠尺寸", max_length=50, blank=True)
    pearl_shape = models.CharField("珍珠形状", max_length=50, blank=True)
    pearl_color = models.CharField("珍珠颜色", max_length=100, blank=True)
    pearl_luster = models.CharField("光泽度", max_length=50, blank=True)
    pearl_quality = models.CharField("品质等级", max_length=50, blank=True)
    material = models.CharField("材质", max_length=200, blank=True)

    base_price = models.DecimalField("基础价格", max_digits=12, decimal_places=2, default=0)
    is_price_from = models.BooleanField("显示起价", default=False)

    cover_image = models.ImageField("封面图", upload_to="products/covers/", blank=True)

    is_active = models.BooleanField("上架", default=True)
    is_featured = models.BooleanField("推荐", default=False)
    is_new = models.BooleanField("新品", default=False)
    sort_order = models.PositiveIntegerField("排序", default=0)

    meta_title = models.CharField("SEO标题", max_length=70, blank=True)
    meta_description = models.CharField("SEO描述", max_length=160, blank=True)

    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        verbose_name = "产品"
        verbose_name_plural = "产品"
        ordering = ["sort_order", "-created_at"]
        indexes = [
            models.Index(fields=["is_active", "is_featured"]),
            models.Index(fields=["pearl_type"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.get_pearl_type_display()})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.name_en or self.name
            self.slug = slugify(base)
            existing = Product.objects.filter(slug=self.slug).exclude(pk=self.pk)
            if existing.exists():
                self.slug = f"{self.slug}-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variants", verbose_name="所属产品"
    )
    sku = models.CharField("SKU", max_length=50, unique=True)
    name = models.CharField("规格名", max_length=100)

    chain_length = models.CharField("链长", max_length=50, blank=True)
    pearl_size = models.CharField("珍珠尺寸", max_length=50, blank=True)
    color_option = models.CharField("颜色选项", max_length=50, blank=True)

    price = models.DecimalField("售价", max_digits=12, decimal_places=2)
    compare_at_price = models.DecimalField("原价", max_digits=12, decimal_places=2,
                                           null=True, blank=True)
    stock = models.PositiveIntegerField("库存", default=0)
    is_default = models.BooleanField("默认SKU", default=False)

    image = models.ImageField("规格图", upload_to="products/variants/", blank=True)

    is_active = models.BooleanField("启用", default=True)
    sort_order = models.PositiveIntegerField("排序", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "SKU"
        verbose_name_plural = "SKU"
        ordering = ["product", "sort_order"]

    def __str__(self):
        return f"{self.sku} -- {self.name}"

    def save(self, *args, **kwargs):
        if not self.sku:
            prefix = self.product.sku_prefix or self.product.pearl_type[:3].upper()
            count = ProductVariant.objects.filter(product=self.product).count() + 1
            self.sku = f"{prefix}-{count:03d}"
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="产品"
    )
    image = models.ImageField("图片", upload_to="products/gallery/")
    alt_text = models.CharField("ALT文本", max_length=200, blank=True)
    sort_order = models.PositiveIntegerField("排序", default=0)
    is_primary = models.BooleanField("主图", default=False)

    class Meta:
        verbose_name = "产品图片"
        verbose_name_plural = "产品图片"
        ordering = ["sort_order"]

    def __str__(self):
        return f"{self.product.name} - 图{self.sort_order}"


class ProductTag(models.Model):
    name = models.CharField("标签名", max_length=50)
    slug = models.SlugField("Slug", unique=True, max_length=60)
    products = models.ManyToManyField(Product, blank=True, related_name="tags")
    is_active = models.BooleanField("启用", default=True)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
