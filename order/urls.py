from django.urls import path, include

from .views import CreateOrderAPI


urlpatterns = [
    path("create/",CreateOrderAPI.as_view(),name = 'order')
]