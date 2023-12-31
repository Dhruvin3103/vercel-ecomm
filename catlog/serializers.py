from rest_framework import serializers
from .models import ProdImage,ProdReview,Product,SubCateorgy,MainCateorgy, WishlistProduct,ProductBySize
from accounts.models import User
from accounts.serializers import UserSerializer

class MainCateorgySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCateorgy
        fields = "__all__"

class SubCateorgySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCateorgy
        fields = "__all__"
        depth = 0
    
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['main_cateorgy'] = MainCateorgySerializer(
    #         MainCateorgy.objects.get(pk=data['main_cateorgy'])).data
    #     return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        depth = 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = [i['image'] for i in ProdImageSerializer(ProdImage.objects.filter(image_fk = data['id']),many=True).data]
        data['sizes'] =     [i for i in ProductBySizeSerializer(ProductBySize.objects.filter(product=data['id']),many=True).data]
        return data

class ProductBySizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBySize
        fields = "__all__"
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['size_name'] = instance.size.name
        data['size_desc'] = instance.size.desc
        del data['product'],data['size']
        return data

class ProdReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdReview
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['review_fk'] = ProductSerializer(
            Product.objects.get(pk=data['review_fk'])).data
        data['reviewed_by'] = UserSerializer(
            User.objects.get(pk=data['reviewed_by'])).data
        return data

class ProdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdImage
        fields = ["image"]
        depth = 0

class WishlistProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistProduct
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        val = ProductSerializer(
            Product.objects.get(pk=data['product'])).data
        return {'id':val['id'], 'name': val['name'], 'price': val['price']}