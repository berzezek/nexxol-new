from django.urls import include, re_path

from .views import CategoryViewSet, ProductViewSet, ImageViewSet, ProductPropertyViewSet, CategoryPropertyViewSet
from rest_framework import routers

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]


router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('images', ImageViewSet, basename='image')
router.register('category-properties', CategoryPropertyViewSet, basename='category-property')
router.register('product-properties', ProductPropertyViewSet, basename='product-property')

urlpatterns += router.urls