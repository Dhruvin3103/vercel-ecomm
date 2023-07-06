from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Orders
# Create your views here.


class CreateOrderAPI(GenericAPIView,CreateModelMixin,ListModelMixin):
    permission_classes = [IsAuthenticated]

    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)
        return queryset

    def get(self,request):
        return self.list(request)

    def post(self, request):
        try:
            return self.create(request)
        except Exception as e:
            return Response({'error' : str(e)})