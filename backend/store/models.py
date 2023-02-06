from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product.image_set.count() >= 5:
            raise Exception('Maximum 5 images')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name


class CategoryProperty(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductProperty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_property = models.ForeignKey(CategoryProperty, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def is_required(self):
        if not self.category_property.is_required:
            self.value = None

    def __str__(self):
        return self.value
