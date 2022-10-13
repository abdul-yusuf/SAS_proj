from django.urls import path
from .views import UserCreate, UserDetails 

urlpatterns = [
    path('user_detail/', UserDetails.as_view(), name='user-detail'),
    path('signup/', UserCreate.as_view(), name='user-signup'),
]
