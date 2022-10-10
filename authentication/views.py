from rest_framework import generics
from . import models, serializers

class UserDetails(generics.GenericAPIView):
    queryset = models.User
    serializer_class = serializers.UserSerializer 