from django.urls import path, include

from .views import CreateOrderAPI,UpdatePaymentStatusAPI


urlpatterns = [
    path("create/",CreateOrderAPI.as_view(),name = 'order'),
    path("update/",UpdatePaymentStatusAPI.as_view(),name = 'order'),
    path("create/<id>",CreateOrderAPI.as_view(),name = 'order')
]