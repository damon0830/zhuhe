from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet, basename="category")
router.register(r"collections", views.CollectionViewSet, basename="collection")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"variants", views.ProductVariantViewSet, basename="variant")
router.register(r"images", views.ProductImageViewSet, basename="image")

urlpatterns = router.urls
