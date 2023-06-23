from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance