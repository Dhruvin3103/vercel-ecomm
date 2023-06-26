from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from .models import ProdImage,ProdReview,Product,SubCateorgy,MainCateorgy
from .serializers import MainCateorgySerializer,SubCateorgySerializer,ProductSerializer,ProdReviewSerializer,ProdImageSerializer

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
        
