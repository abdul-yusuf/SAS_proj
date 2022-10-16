from rest_framework import generics, viewsets
from django.shortcuts import render
from . import models, serializers

# Create your views here.

# class ProductView(generics.ListCreateAPIView):
class ProductView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ReviewCreate(generics.CreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    # def post(self, request, *args, **kwargs):



    #     return super().post(request, *args, **kwargs)

