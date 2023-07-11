from django.forms import ValidationError
from rest_framework import serializers
from .models import Orders
from accounts.models import User
from catlog.models import Product
from django.db import transaction
from accounts.serializers import UserSerializer
from accounts.models import User,Address
# from BaseException im
from time import sleep


class CustomValidationError(ValidationError):
    def __str__(self):
        # Custom error message format
        return " Error: "+self.message

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ["count","payment_status","product","payment_type"]



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
