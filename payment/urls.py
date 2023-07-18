from django.urls import path
from .views import TransactionAPIView,TransactionForCartAPIView

urlpatterns = [
    path("complete/", TransactionAPIView.as_view(), name="razorpay-complete-order-api"),
    path("cart/complete/", TransactionForCartAPIView.as_view(), name="razorpay-complete-cart-order-api")
    
]