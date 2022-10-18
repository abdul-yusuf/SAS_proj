from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ordered-item', views.AddItemToCart, basename='ordered-item')

urlpatterns = [
    # path('', include(router.urls))
    # path('ordered-item', views.AddItemToCart.as_view(), name='ordered-item'),
]

urlpatterns += router.urls
