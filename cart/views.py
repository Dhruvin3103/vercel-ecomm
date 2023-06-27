from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from .models import Cart,Product_cart
from .serializers import CartSerializer,ProductCartSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

class CartAPI(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request):
        serializer = CartSerializer(Cart.objects.get(user = request.user.id)) 
        return Response(serializer.data)
    
class ProductCartAPI(GenericAPIView,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = Product_cart.objects.all()
    serializer_class = ProductCartSerializer

    def post(self, request):
        return self.create(request)
    