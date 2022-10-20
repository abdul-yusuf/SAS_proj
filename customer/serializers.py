from rest_framework import serializers

# from marchant.functions import attempt_json_deserialize
from . import models

class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = '__all__'

