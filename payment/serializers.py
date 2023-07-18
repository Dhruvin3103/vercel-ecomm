from rest_framework import serializers
from .models import Transaction


class RazorpayOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()


class TranscationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ["payment_id", "order_id_1","order_id_2", "signature", "amount"]
        
# class TranscationForCartModelSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Transaction_Cart
#         fields = ["payment_id", "order_id_1","order_id_2", "signature", "amount"]
#         depth = 1