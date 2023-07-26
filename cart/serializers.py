from rest_framework import serializers
from catlog.models import Product
from catlog.serializers import ProductSerializer
from .models import Product_cart
from catlog.models import ProductBySize

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_cart
        fields = ["id","count","product_by_size"]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        product = ProductBySize.objects.get(id=data['product_by_size'])
        # print(product.product.price)
        # print(instance.user.id,(Product.objects.filter(id=data['product']).values()[0]['product']))
        available = product.available_count
        data['product'] = product.product.id
        data['product_price'] = product.product.price
        data['total_price'] = product.product.price * data['count']
        return data


        # data['total_price'] = data['cart']
        # data['product'] = ProductSerializer(
        #     Product.objects.get(pk=data['product'])).data
        # return data

        