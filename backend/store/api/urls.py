from .views import CategoryViewSet, ProductViewSet, ImageViewSet, ProductPropertyViewSet, CategoryPropertyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('images', ImageViewSet, basename='image')
router.register('category-properties', CategoryPropertyViewSet, basename='category-property')
router.register('product-properties', ProductPropertyViewSet, basename='product-property')

urlpatterns = router.urls