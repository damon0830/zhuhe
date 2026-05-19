import uuid, re
from django.db import models
from django.conf import settings


class Order(models.Model):
    """订单"""
    class Status(models.TextChoices):
        PENDING = "pending", "待付款"
        CONFIRMED = "confirmed", "已确认"
        PROCESSING = "processing", "处理中"
        SHIPPED = "shipped", "已发货"
        DELIVERED = "delivered", "已送达"
        CANCELLED = "cancelled", "已取消"
        REFUNDED = "refunded", "已退款"

    order_number = models.CharField("订单号", max_length=30, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name="用户", related_name="orders"
    )
    email = models.EmailField("邮箱")
    status = models.CharField("状态", max_length=20, choices=Status.choices, default=Status.PENDING)

    # 地址快照 (JSON)
    shipping_address = models.JSONField("收货地址", default=dict)
    billing_address = models.JSONField("账单地址", default=dict)

    # 金额
    subtotal = models.DecimalField("小计", max_digits=12, decimal_places=2, default=0)
    shipping_cost = models.DecimalField("运费", max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField("税费", max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField("总计", max_digits=12, decimal_places=2, default=0)
    currency = models.CharField("货币", max_length=3, default="EUR")

    notes = models.TextField("备注", blank=True)

    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)
    paid_at = models.DateTimeField("付款时间", null=True, blank=True)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "-created_at"]),
            models.Index(fields=["status"]),
            models.Index(fields=["order_number"]),
        ]

    def __str__(self):
        return f"Order {self.order_number} ({self.get_status_display()})"

    def save(self, *args, **kwargs):
        if not self.order_number:
            today = self.created_at or __import__("django").utils.timezone.now()
            prefix = f"ZH-{today.strftime('%Y%m%d')}-"
            last_num = Order.objects.filter(order_number__startswith=prefix).count() + 1
            self.order_number = f"{prefix}{last_num:05d}"
        super().save(*args, **kwargs)

    @property
    def items_count(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    """订单商品"""
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items",
        verbose_name="订单"
    )
    variant = models.ForeignKey(
        "products.ProductVariant", on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name="SKU"
    )

    # 快照
    product_name = models.CharField("商品名", max_length=200)
    variant_name = models.CharField("规格名", max_length=100, blank=True)
    sku = models.CharField("SKU", max_length=50, blank=True)
    product_image = models.URLField("商品图片", blank=True)

    price = models.DecimalField("单价", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("数量", default=1)
    subtotal = models.DecimalField("小计", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = "订单商品"

    def __str__(self):
        return f"{self.sku} x{self.quantity}"

    def save(self, *args, **kwargs):
        self.subtotal = self.price * self.quantity
        super().save(*args, **kwargs)
