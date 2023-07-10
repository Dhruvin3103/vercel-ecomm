from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Orders,Product
from payment.razorpay import RazorpayClient

rz_client = RazorpayClient()
# Create your views here.


class CreateOrderAPI(GenericAPIView,CreateModelMixin,ListModelMixin,DestroyModelMixin):
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset
    
    def get(self,request):
        return self.list(request)


    def delete(self,request,id):
        return self.destroy(request,id)
    def post(self, request):
        try:
            data = self.create(request).data
            print(data["payment_type"])
            if data["payment_type"] == "1":
                amount = data["count"]*Product.objects.filter(id = data["product"]).values()[0]['price']
                print(amount)
                order_response = rz_client.create_order(
                    amount=amount,
                    currency= "INR"
                )
                return Response(
                    {"data" : data,
                    "order_data":order_response}
                )
            elif data["payment_type"] == "2":
                return Response({"data":data})
        except Exception as e:
            return Response({'error' : str(e)})