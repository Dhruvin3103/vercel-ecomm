from rest_framework import serializers
from catlog.models import Product
from catlog.serializers import ProductSerializer
from .models import Product_cart,Cart

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = "__all__"
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['total_price'] = 0
#         data['product-data'] = []
#         for i in ProductCartSerializer(Product_cart.objects.filter(cart = data['id']),many=True).data:
#             data['total_price'] += i['product']['price']*i['count']
#             data['product-data'] += [{'id':i['product']['id'],'name':i['product']['name'],'color':i['product']['color'],'price':i['product']['price'],'count':i['count'],'size':i['size']}]
#         return data

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_cart
        fields = ["id","size","count","product"]
        
    def create(self, validated_data):
        data = super().create(validated_data)
        request = self.context.get('request')
        user = request.user
        cart = Cart.objects.filter(user=user).first()
        print(data.id)
        product_cart = Product_cart.objects.get(id=data.id)
        product_data = Product.objects.filter(id=request.data['product']).values()[0]
        print(type(product_data['price']),type(request.data['count']))
        # print(data,Product_cart.objects.get(user=user,product=data.data['product'],size=data.data['size']))
        if cart!=None:
            cart = Cart.objects.get(user=user)
            cart.cart_price += int(product_data['price'])*int(request.data['count'])
            cart.save()
            cart.product.add(product_cart)
        else:
            cart = Cart(user=user,cart_price=int(product_data['price'])*int(request.data['count']))
            cart.save()
            cart.product.add(product_cart)
            cart.save()
        return data
    # def to_representation(self, instance):
    #     request = self.context.get('request')
    #     user = request.user
    #     data = super().to_representation(instance)
    #     price = Product.objects.filter(id=data['product']).values()[0]
    #     # print(instance.user.id,(Product.objects.filter(id=data['product']).values()[0]['price']))
    #     available = price['available_count']
        
    #     data['product_price'] = price['price']
    #     data['total_price'] = price['price'] * data['count']
    #     cart = Cart.objects.get(user=user)
    #     # product_cart = Product_cart.objects.get(user=user,product=request.data['product'],size=request.data['size'])
    #     # cart.product.add(product_cart)
    #     print(Product_cart.objects.all().values())
    #     return data

        
