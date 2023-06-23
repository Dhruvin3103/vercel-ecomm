from rest_framework import serializers
from .models import ProdImages,ProdReview,Products,SubCateorgy,MainCateorgy

class MainCateorgySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCateorgy
        fields = "__all__"

class SubCateorgySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCateorgy
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class ProdReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdReview
        fields = "__all__"

class ProdImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdImages
        fields = "__all__"