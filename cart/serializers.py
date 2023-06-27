from rest_framework import serializers
from catlog.models import Product
from catlog.serializers import ProductSerializer
from .models import Cart,Product_cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_price'] = 0
        data['product-data'] = []
        for i in ProductCartSerializer(Product_cart.objects.filter(cart = data['id']),many=True).data:
            data['total_price'] += i['product']['price']*i['count']
            data['product-data'] += [{'id':i['product']['id'],'name':i['product']['name'],'color':i['product']['color'],'price':i['product']['price'],'count':i['count'],'size':i['size']}]
        return data

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_cart
        fields = "__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['cart'] = data['cart']
        data['product'] = ProductSerializer(
            Product.objects.get(pk=data['product'])).data
        return data

        
