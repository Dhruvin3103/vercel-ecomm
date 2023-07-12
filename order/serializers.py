from django.forms import ValidationError
from rest_framework import serializers
from .models import Orders
from accounts.models import User
from catlog.models import Product
from django.db import transaction
from accounts.serializers import UserSerializer
from accounts.models import User,Address
from cart.models import Product_cart
# from BaseException im
from time import sleep


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
        for i in instance:
            amount += instance[i].product.price*instance[i].count
        return {"amount":str(amount),"payment_type":request.data['payment_type']}
#serialzer when user do instant buy now
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["id","count","payment_status","product","payment_type"]

    def create(self,validated_data):
        try:
            # sleep(5)
            with transaction.atomic():
                request = self.context.get('request')
                user = request.user
                print('address' in request.data)
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
                product = Product.objects.select_for_update().get(id = validated_data['product'].id)
                print(validated_data,request.data)
                if (product.available_count) >= validated_data['count']: 
                    product.available_count -= validated_data['count']
                    product.save()
                    return super().create(validated_data)
                else:
                    raise CustomValidationError('sry')
        except Exception as e:
            raise e
# {'count': 4, 'status': '1', 'product': <Product: red tshirt id : 1 20>, 'user': <User: admin@gmail.com, +919967118952>, 'address': <Address: dhruvinhemant5, None 2>}
