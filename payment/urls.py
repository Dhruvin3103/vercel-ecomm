from django.urls import path
from .views import TransactionAPIView,TransactionForCartAPIView,TransactionGetAPIView

urlpatterns = [
    path("complete/", TransactionAPIView.as_view(), name="razorpay-complete-order-api"),
    path("cart/complete/", TransactionForCartAPIView.as_view(), name="razorpay-complete-cart-order-api"),
    path("trans/get/",TransactionGetAPIView.as_view(),name='Transc-Get')
    
]