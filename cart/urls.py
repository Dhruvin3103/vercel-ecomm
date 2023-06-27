from django.urls import path, include
from .views import CartAPI,ProductCartAPI

urlpatterns = [
    path('', CartAPI.as_view(), name = 'Cart-view'),
    path('productcart/',ProductCartAPI.as_view(),name='Product cart View')
]