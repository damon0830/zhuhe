from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Collection, Product, ProductVariant, ProductImage
from .serializers import CategorySerializer, CollectionSerializer, ProductListSerializer, ProductDetailSerializer, ProductVariantSerializer, ProductImageSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = "slug"


class CollectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Collection.objects.filter(is_active=True)
    serializer_class = CollectionSerializer
    lookup_field = "slug"

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params.get("featured"):
            qs = qs.filter(is_featured=True)
        return qs


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {"pearl_type": ["exact"], "category__slug": ["exact"], "collections__slug": ["exact"], "is_featured": ["exact"], "is_new": ["exact"], "base_price": ["gte", "lte"]}
    search_fields = ["name", "name_en", "description", "short_description"]
    ordering_fields = ["base_price", "created_at", "sort_order", "name"]
    ordering = ["sort_order", "-created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer
        return ProductDetailSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.prefetch_related("images", "variants", "tags", "collections").select_related("category")


class ProductVariantViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductVariant.objects.filter(is_active=True)
    serializer_class = ProductVariantSerializer
    filterset_fields = ["product__slug", "is_default"]


class ProductImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filterset_fields = ["product__slug", "is_primary"]
    ordering = ["sort_order"]
