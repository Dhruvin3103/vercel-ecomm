from django.urls import path, include
from .views import ProductCartAPI,UpdateDeleteProductCartAPI

urlpatterns = [
    # path('', CartAPI.as_view(), name = 'Cart-view'),
    path('productcart/',ProductCartAPI.as_view(),name='Product cart View'),
    path('updatecart/',UpdateDeleteProductCartAPI.as_view(),name='Update cart View')
]