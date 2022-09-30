from django.urls import path
from .views import Logout, Login, SignUp


app_name = 'authentication'
urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', SignUp, name='register'),
    path('logout/', Logout, name='logout'),
    
]
