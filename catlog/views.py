from django.shortcuts import render
from rest_framework import mixins, generics, authentication
# from rest_framework.response import response
from .models import ProdImages,ProdReview,Products,SubCateorgy,MainCateorgy
from .serializers import MainCateorgySerializer,SubCateorgySerializer,ProductSerializer,ProdReviewSerializer,ProdImagesSerializer
from rest_framework import viewsets


class MainCateorgyAPI(viewsets.ModelViewSet):
    serializer_class = MainCateorgySerializer
    queryset = MainCateorgy.objects.all()