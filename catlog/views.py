from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from .models import ProdImage,ProdReview,Product,SubCateorgy,MainCateorgy,WishlistProduct
from .serializers import MainCateorgySerializer,SubCateorgySerializer,ProductSerializer,ProdReviewSerializer,ProdImageSerializer,WishlistProductSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MainCateorgyAPI(GenericAPIView, ListModelMixin):
    serializer_class = MainCateorgySerializer
    queryset = MainCateorgy.objects.all()
    def get(self, request):
        return self.list(request)

class SubCateorgyAPI(GenericAPIView):
    serializer_class = SubCateorgySerializer
    queryset = SubCateorgy.objects.all()
    def get(self, request, main_cat_id):
        serializer = SubCateorgySerializer(SubCateorgy.objects.filter(main_cateorgy = main_cat_id),many=True)
        return Response(serializer.data)

class ProductAPI(GenericAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    def get(self, request, sub_cat_id):
        serializer = ProductSerializer(Product.objects.filter(sub_cateorgy = sub_cat_id),many=True) 
        return Response(serializer.data)
    
class WishlistProductAPI(GenericAPIView, CreateModelMixin, ListModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WishlistProductSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = WishlistProduct.objects.filter(user=user)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        try:
            serializer = self.serializer_class(data = {'user' : request.user.id,'product':request.data['product']})
            if not serializer.is_valid():
                return Response(serializer.errors)
            serializer.save()
            return Response({'response':'added to whishlist'})
        except Exception as e:
            return Response({"error":str(e)})
        
    def delete(self, request):
        try:
            WishlistProduct.objects.get(user = request.user.id, product = request.data['product']).delete()
            return Response({'response':'deleted successfully'})
        except Exception as e:
            return Response({"error":str(e)})
