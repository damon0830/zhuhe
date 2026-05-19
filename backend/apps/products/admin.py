from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Collection, Product, ProductVariant, ProductImage, ProductTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "sort_order", "is_active"]
    list_editable = ["sort_order", "is_active"]
    prepopulated_fields = {"slug": ["name_en", "name"]}
    search_fields = ["name", "name_en"]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["name", "is_featured", "sort_order", "is_active"]
    list_editable = ["is_featured", "sort_order", "is_active"]
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ["name"]


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    fields = ["sku", "name", "price", "stock", "is_default", "is_active"]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2
    fields = ["image_preview", "image", "sort_order", "is_primary"]
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;width:auto;" />', obj.image.url)
        return "-"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "pearl_type", "base_price", "is_active", "is_featured", "is_new"]
    list_editable = ["base_price", "is_active", "is_featured", "is_new"]
    list_filter = ["is_active", "is_featured", "is_new", "pearl_type", "category"]
    search_fields = ["name", "name_en", "sku_prefix", "description"]
    prepopulated_fields = {"slug": ["name_en", "name"]}
    inlines = [ProductVariantInline, ProductImageInline]
    fieldsets = [
        ("基本信息", {"fields": ["name", "name_en", "slug", "sku_prefix", "description", "short_description", "category", "collections"]}),
        ("珍珠规格", {"fields": ["pearl_type", "pearl_size", "pearl_shape", "pearl_color", "pearl_luster", "pearl_quality", "material"]}),
        ("价格与媒体", {"fields": ["base_price", "is_price_from", "cover_image"]}),
        ("状态", {"fields": ["is_active", "is_featured", "is_new", "sort_order"]}),
        ("SEO", {"fields": ["meta_title", "meta_description"]}),
    ]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ["sku", "product", "name", "price", "stock", "is_default", "is_active"]
    list_editable = ["price", "stock", "is_default", "is_active"]
    list_filter = ["is_active", "product"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["product", "sort_order", "is_primary"]
    list_editable = ["sort_order", "is_primary"]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active"]
    prepopulated_fields = {"slug": ["name"]}
