from django.shortcuts import render
from rest_framework import mixins, generics, authentication
from rest_framework.response import response
from .models import ProdImages,ProdReview,Products,SubCateorgy,MainCateorgy
from .serializers import MainCateorgySerializer,SubCateorgySerializer,ProductSerializer,ProdReviewSerializer,ProdImagesSerializer

class MainCateorgyAPI(generics.GenericAPIView):
    queryset = MainCateorgy.objects.all()
    serializer_class = MainCateorgySerializer
    
