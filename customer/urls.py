from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ordered-item', views.AddItemToCart, basename='ordered-item')
# router.register('payment', views.Payment_RUD, basename='payment-cruds')

urlpatterns = [
    path('payment', views.Payment_RUD.as_view(), name='payment-cruds'),
    path('payment_verify', views.Payment_verify.as_view(), name='payment-verify'),
    path('payment_create', views.Payment_Create.as_view(), name='payment-create')
    # path('ordered-item', views.AddItemToCart.as_view(), name='ordered-item'),
]

urlpatterns += router.urls
