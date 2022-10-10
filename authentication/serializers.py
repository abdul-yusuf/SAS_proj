from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_no', 'nationality', 'state_of_origin', 'business_state', 'local_govt', 'specialization', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User(
    #     email=validated_data['email'],
    #     username=validated_data['username'],
    #     phone_no=validated_data['phone_no']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user