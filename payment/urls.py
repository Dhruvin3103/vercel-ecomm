from django.urls import path
from .views import TransactionAPIView

urlpatterns = [
    path("complete/", 
        TransactionAPIView.as_view(), 
        name="razorpay-complete-order-api"
    )
]