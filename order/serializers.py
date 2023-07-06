from django.forms import ValidationError
from rest_framework import serializers
from .models import Orders
from accounts.models import User
from catlog.models import Product
from django.db import transaction
from accounts.serializers import UserSerializer
# from BaseException im
from time import sleep

class CustomValidationError(ValidationError):
    def __str__(self):
        # Custom error message format
        return "Custom Validation Error: {sry out of stock}"

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def create(self,validated_data):
        try:
            with transaction.atomic():
                product = Product.objects.get(id = validated_data['product'].id)
                print(validated_data)
                
                if (product.available_count) >= validated_data['count'] :
                    product.available_count -= validated_data['count']
                    sleep(5)
                    product.save()
                    return super().create(validated_data)
                else:
                    raise CustomValidationError('sry')
        except Exception as e:
            raise e
# {'count': 4, 'status': '1', 'product': <Product: red tshirt id : 1 20>, 'user': <User: admin@gmail.com, +919967118952>, 'address': <Address: dhruvinhemant5, None 2>}