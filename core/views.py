from rest_framework import generics
from django.shortcuts import render
from . import models, serializers

# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class Sub_ProductView(generics.ListCreateAPIView):
    queryset = models.Sub_Product.objects.all()
    serializer_class = serializers.Sub_ProductSerializer
