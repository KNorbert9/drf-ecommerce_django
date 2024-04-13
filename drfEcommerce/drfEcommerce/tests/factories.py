import factory
from drfEcommerce.product.models import Category, Brand, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('name',)
        
        
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
        django_get_or_create = ('name',)
        
        
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        django_get_or_create = ('name',)