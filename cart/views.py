from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from .models import Product_cart
from .serializers import ProductCartSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

# class CartAPI(GenericAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def get(self, request):
#         serializer = CartSerializer(Cart.objects.get(user = request.user.id)) 
#         return Response(serializer.data)
    
    
class ProductCartMixin(ListModelMixin,CreateModelMixin):
        def get_queryset(self):
            queryset = Product_cart.objects.all()
            user_id = self.request.query_params.get('id')
            if user_id:
                queryset = queryset.filter(user=user_id)
            return queryset

class ProductCartAPI(ListCreateAPIView,ProductCartMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCartSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product_cart.objects.filter(user=user)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']
        size = serializer.validated_data['size']
        count = serializer.validated_data['count']

        try:
            # Check if the product already exists in the user's cart
            cart_item = Product_cart.objects.get(user=user, product=product, size = size)
            # Increment the count of the existing cart item
            cart_item.count += count
            cart_item.save()
        except Product_cart.DoesNotExist:
            serializer.save(user=user)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    