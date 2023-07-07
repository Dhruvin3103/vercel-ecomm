from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .serializers import OrdersSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Orders
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
            return self.create(request)
        except Exception as e:
            return Response({'error' : str(e)})