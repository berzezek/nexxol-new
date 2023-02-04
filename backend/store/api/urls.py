from .views import CategoryViewSet, ProductViewSet, ImageViewSet, ProductPropertyViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('images', ImageViewSet, basename='image')
router.register('productproperties', ProductPropertyViewSet, basename='productproperty')

urlpatterns = router.urls