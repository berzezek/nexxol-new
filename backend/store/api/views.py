from ..models import Category, Product, Image, CategoryProperty, ProductProperty
from .serializers import CategorySerializer, ProductSerializer, ImageSerializer, CategoryPropertySerializer, ProductPropertySerializer
from rest_framework import viewsets, permissions

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Image.objects.all()
        product_id = self.request.query_params.get('product_id', None)
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset


class CategoryPropertyViewSet(viewsets.ModelViewSet):
    queryset = CategoryProperty.objects.all()
    serializer_class = CategoryPropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductPropertyViewSet(viewsets.ModelViewSet):
    queryset = ProductProperty.objects.all()
    serializer_class = ProductPropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
