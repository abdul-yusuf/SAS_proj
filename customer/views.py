from django.shortcuts import render
from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, viewsets, views

# Create your views here.

class AddItemToCart(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderedItemSerializer
    # get_extra_actions = 
    permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     cart = models.OrderItem.objects.filter(user=request.user)
    #     data = serializers.OrderItemSerializer(cart, many=True).data
    #     return Response(data)

    # def post(self, request):


