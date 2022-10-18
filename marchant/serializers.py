from rest_framework import serializers

from marchant.functions import attempt_json_deserialize
from . import models

class ReviewReplySerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ReviewReply
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    # reply= ReviewReplySerializer(many=True)
    reply = serializers.PrimaryKeyRelatedField(queryset=models.ReviewReply, many=True)

    class Meta:
        model = models.Review
        fields = ('id','body','user','reply','rating','rate')
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    review_set = serializers.PrimaryKeyRelatedField(queryset=models.Review.objects.all(), many=True)
    # review = ReviewSerializer(read_only=True)
    rating = RatingSerializer(read_only=True)
    images = ImageSerializer(read_only=True)
    class Meta:
        model = models.Product
        fields = ('id','title','category','timeframe','size','value','images','rating','review_set','rate')
        dept = 1
    def create(self, validated_data):
        request = self.context['request']

        rating_data = request.data.get('rating')
        rating_data = attempt_json_deserialize(rating_data, expect_type=dict)
        rating = models.Rating.objects.create(**rating_data)
        validated_data['rating'] = rating
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        request = self.context['request']

        rating_data = request.data.get('rating')
        rating_data = attempt_json_deserialize(rating_data, expect_type=dict)
        rating = models.Rating.objects.create(**rating_data)
        validated_data['rating'] = rating

        review_data = request.data.get('review')
        review_data = attempt_json_deserialize(review_data, expect_type=list)
        review = models.Review.objects.create(**review_data)
        validated_data['review'] = review
        
        return super().update(instance, validated_data)

