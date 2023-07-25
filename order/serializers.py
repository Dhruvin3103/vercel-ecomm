from django.forms import ValidationError
from rest_framework import serializers
from .models import Orders
from accounts.models import User
from catlog.models import ProductBySize,Product
from django.db import transaction
from accounts.serializers import UserSerializer
from accounts.models import User,Address
from cart.models import Product_cart
# from BaseException im
from time import sleep


class UpdatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id"]

class CustomValidationError(ValidationError):
    def __str__(self):
        return " Error: "+self.message

#serializer when make order through cart
class CartOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id","payment_status","payment_type"]

    def create(self,validated_data):
        try:
            # sleep(5)
            with transaction.atomic():
                #taking user id from request
                request = self.context.get('request')
                user = request.user
                #checking of address
                if 'address' in request.data:
                    address = Address.objects.get(id=request.data['address'])
                    if address.user == user:
                        pass
                    else:
                        raise CustomValidationError('sry')
                else:               
                    address = Address.objects.filter(user=user).first()
                validated_data['user'] = user
                if address != None:
                    validated_data['address'] = address
                else:
                    raise CustomValidationError(message="user has not entered any address in profile")

                product_cart_data = Product_cart.objects.filter(user =user)
                print(len(product_cart_data)==0)
                # print(product_cart_data)
                if len(product_cart_data)!=0:
                    prod_dict = {}
                    for data in product_cart_data:
                        product = Product.objects.select_for_update().get(id = data.product_id)
                        validated_data['product'] = data.product
                        validated_data['count'] = data.count
                        validated_data['size'] = data.size
                        print(validated_data)
                        if (product.available_count) >= data.count: 
                            print("in if")
                            product.available_count -= data.count
                            product.save()
                            prod_dict[data.id] = super().create(validated_data)
                            data.delete()
                        else:
                            print("in else")
                            raise CustomValidationError(f'{validated_data["product"]}')
                    return prod_dict
                else:
                    raise CustomValidationError("You cart is empty")
                # print(prod_dict)
                
        except Exception as e:
            raise e

    def to_representation(self, instance):
        request = self.context.get('request')
        amount = 0
        ids = []
        for i in instance:
            amount += instance[i].product.price*instance[i].count
            ids.append(instance[i].id)
        return {"amount":str(amount),"payment_type":request.data['payment_type'],"order_ids":str(ids)}
#serialzer when user do instant buy now
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id","count","payment_status","product_by_size","payment_type"]

    def create(self,validated_data):
        try:
            # sleep(5)
            with transaction.atomic():
                request = self.context.get('request')
                user = request.user
                # print('address' in request.data)
                if 'address' in request.data:
                    address = Address.objects.get(id=request.data['address'])
                    if address.user == user:
                        pass
                    else:
                        raise CustomValidationError('sry address issue')
                else:               
                    address = Address.objects.filter(user=user).first()
                validated_data['user'] = user
                if address != None:
                    validated_data['address'] = address
                else:
                    raise CustomValidationError(message="user has not entered any address in profile")
                product = ProductBySize.objects.select_for_update().get(id = validated_data['product_by_size'].id)
                # print(validated_data,request.data)
                if (product.available_count) >= validated_data['count']: 
                    product.available_count -= validated_data['count']
                    price = Product.objects.get(id= validated_data['product_by_size'].product.id).price
                    amount = validated_data["count"]*price
                    print(amount)
                    product.save()
                    return super().create(validated_data)
                else:
                    raise CustomValidationError('sry stock that product got sold out')
        except Exception as e:
            raise e
    
    def to_representation(self, instance):
        print(instance.product_by_size.product.id)
        price = Product.objects.get(id= instance.product_by_size.product.id).price
        amount = instance.count*price
        
        # instance['amount'] = amount
        return {
            "id": instance.id,
            "count": instance.count,
            "payment_status": instance.payment_status,
            "product_by_size": instance.product_by_size.id,
            "payment_type": instance.payment_type,
            "amount":amount
        }
# {'count': 4, 'status': '1', 'product': <Product: red tshirt id : 1 20>, 'user': <User: admin@gmail.com, +919967118952>, 'address': <Address: dhruvinhemant5, None 2>}
