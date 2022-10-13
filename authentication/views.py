from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models, serializers

class UserDetails(generics.RetrieveAPIView):
    """_summary_

    Args:
        generics (_type_): _description_
    """
    queryset = models.User
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

class UserCreate(generics.CreateAPIView):
    queryset = models.User
    serializer_class = serializers.UserSerializer