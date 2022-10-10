from django.urls import path
from . import views

urlpatterns = [
    path('user_detail', views.UserDetails.as_view(), name='user-detail'),
]
