from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import RazorpayOrderSerializer,TranscationModelSerializer
from rest_framework.response import Response
from payment.razorpay import RazorpayClient
from order.models import Orders

rz_client = RazorpayClient()


class TransactionAPIView(APIView):
    """This API will complete order and save the 
    transaction"""
    
    def post(self, request):
        transaction_serializer = TranscationModelSerializer(data=request.data)
        if transaction_serializer.is_valid():
            rz_client.verify_payment_signature(
                razorpay_payment_id = transaction_serializer.validated_data.get("payment_id"),
                razorpay_order_id = transaction_serializer.validated_data.get("order_id_1"),
                razorpay_signature = transaction_serializer.validated_data.get("signature")
            )
            transaction_serializer.save()
            response = {
                "status_code": status.HTTP_201_CREATED,
                "message": "transaction created"
            }
            order = Orders.objects.get(id = request.data["order_id_2"])
            order.payment_status = "1"
            order.save()
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "error": transaction_serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)