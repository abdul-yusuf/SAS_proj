from rest_framework import serializers

# from django.contrib.auth.models import User
from .models import User
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer

class UserRegisterSerializer(
                            # RegisterSerializer,
                            serializers.ModelSerializer,
                            RegisterSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_no', 'nationality', 'state_of_origin', 'business_state', 'local_govt', 'specialization', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()
        data = {
            'email': self.validated_data.get('email', ''),
            'phone_no': self.validated_data.get('phone_no', ''),
            'nationality': self.validated_data.get('nationlity', ''),
            'state_of_origin': self.validated_data.get('state_of_origin', ''),
            'business_state': self.validated_data.get('business_state', ''),
            'local_govt': self.validated_data.get('local_govt', ''),
            'specialization': self.validated_data.get('specialization', ''),
            'password': self.validated_data.get('password', '')
        }
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_no', 'nationality', 'state_of_origin', 'business_state', 'local_govt', 'specialization', 'password')
        # fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User(
        email=validated_data['email'],
        username=validated_data['username'],
        phone_no=validated_data['phone_no'],
        nationality=validated_data['nationality'],
        state_of_origin=validated_data['state_of_origin'],
        business_state=validated_data['business_state'],
        local_govt=validated_data['local_govt'],
        specialization=validated_data['specialization']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
