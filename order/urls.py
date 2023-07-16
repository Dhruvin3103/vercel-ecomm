from django.urls import path, include

from .views import CreateOrderAPI,CreateCartOrderAPI


urlpatterns = [
    path("create/",CreateOrderAPI.as_view(),name = 'order'),
    path("cart/create/",CreateCartOrderAPI.as_view(),name = 'cart_order'),
    path("create/<id>",CreateOrderAPI.as_view(),name = 'order')
]