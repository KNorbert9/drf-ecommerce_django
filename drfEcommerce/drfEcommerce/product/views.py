from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .models import Product, Category, Brand

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def list(self, request):
        serializers = self.serializer_class(self.queryset, many=True)
        return Response(serializers.data)
    
    
class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
    def list(self, request):
        serializers = self.serializer_class(self.queryset, many=True)
        return Response(serializers.data)
    
    
class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def list(self, request):
        serializers = self.serializer_class(self.queryset, many=True)
        return Response(serializers.data)