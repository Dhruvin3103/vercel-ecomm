from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin,DestroyModelMixin,UpdateModelMixin
from .models import Product_cart
from .serializers import ProductCartSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UpdateDeleteProductCartAPI(GenericAPIView):
    serializer_class = ProductCartSerializer

    def patch(self,request):
        serializer = self.serializer_class(Product_cart.objects.get(user = request.user.id,product=request.data['product'],size = request.data['size']),data=request.data,partial =True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.validated_data['count'] = request.data['count']
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request):
        try:
            Product_cart.objects.get(user = request.user.id, product = request.data['product'],size = request.data['size']).delete()
            return Response({'response':'deleted successfully'})
        except Exception as e:
            return Response({"error":str(e)})
        


class ProductCartMixin(ListModelMixin,CreateModelMixin):
        def get_queryset(self):
            queryset = Product_cart.objects.all()
            user_id = self.request.query_params.get('id')
            if user_id:
                queryset = queryset.filter(user=user_id)
            return queryset

class ProductCartAPI(ListCreateAPIView,ProductCartMixin,UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductCartSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Product_cart.objects.filter(user=user)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']
        count = serializer.validated_data['count']
        lookup_field = 'product'

        try:
            # Check if the product already exists in the user's cart
            cart_item = Product_cart.objects.get(user=user, product=product)
            # Increment the count of the existing cart item
            cart_item.count += count
            cart_item.save()
        except Product_cart.DoesNotExist:
            serializer.save(user=user)

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    

    # def perform_destroy(self, serializer):
    #     user = self.request.user
    #     product = serializer.validated_data['product']
    #     size = serializer.validated_data['size']
    #     count = serializer.validated_data['count']

    #     try:
    #         # Check if the product already exists in the user's cart
    #         cart_item = Product_cart.objects.get(user=user, product=product, size = size)
    #         # Increment the count of the existing cart item
    #         cart_item.count += count
    #         cart_item.save()
    #     except Product_cart.DoesNotExist:
    #         serializer.save(user=user)
    