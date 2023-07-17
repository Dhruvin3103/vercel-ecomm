from rest_framework import serializers
from .models import User, Address
from uuid import uuid4

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.is_active = True
        instance.set_password(validated_data['password'])
        instance.email_token = uuid4(),
        instance.save()
        return instance

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        # exclude = ['user']

        fields = ["id","address_line_1","city","pincode","state","country"]

