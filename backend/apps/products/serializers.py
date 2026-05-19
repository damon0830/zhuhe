from rest_framework import serializers
from .models import Category, Collection, Product, ProductVariant, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image", "alt_text", "sort_order", "is_primary"]


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "sku", "name", "chain_length", "pearl_size", "color_option", "price", "compare_at_price", "stock", "is_default", "image", "is_active"]


class ProductListSerializer(serializers.ModelSerializer):
    pearl_type_display = serializers.CharField(source="get_pearl_type_display", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True, default="")

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "short_description", "pearl_type", "pearl_type_display", "pearl_size", "pearl_color", "base_price", "is_price_from", "cover_image", "is_featured", "is_new", "category_name", "created_at"]


class ProductDetailSerializer(serializers.ModelSerializer):
    pearl_type_display = serializers.CharField(source="get_pearl_type_display", read_only=True)
    category = serializers.StringRelatedField()
    collections = serializers.StringRelatedField(many=True)
    images = ProductImageSerializer(many=True, read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "name_en", "slug", "description", "short_description", "category", "collections", "pearl_type", "pearl_type_display", "pearl_size", "pearl_shape", "pearl_color", "pearl_luster", "pearl_quality", "material", "base_price", "is_price_from", "cover_image", "images", "variants", "tags", "is_featured", "is_new", "meta_title", "meta_description", "created_at", "updated_at"]


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "description", "image", "sort_order", "product_count"]

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()


class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ["id", "name", "slug", "description", "subtitle", "image", "bg_gradient", "is_featured", "product_count"]

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()
