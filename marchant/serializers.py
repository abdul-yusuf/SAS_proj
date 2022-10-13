from dataclasses import field
from rest_framework import serializers
from . import models

class Sub_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubProduct
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    sub_product = Sub_ProductSerializer(many=True)
    class Meta:
        model = models.Product
        fields = '__all__'

