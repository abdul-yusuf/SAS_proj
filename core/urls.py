from django.urls import path
from . import views

urlpatterns = [
    path('view', views.ProductView.as_view(), name='products'),
    path('view2', views.Sub_ProductView.as_view(), name='sub-products')
]
