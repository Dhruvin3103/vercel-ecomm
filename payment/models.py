from django.db import models
from order.models import Orders
from accounts.models import User


class Transaction(models.Model):
    payment_id = models.CharField(max_length=200, verbose_name="Payment ID")
    order_id_1 = models.CharField(max_length=200, verbose_name="Order ID")
    order_id_2 = models.ManyToManyField(Orders)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    signature = models.CharField(max_length=500, verbose_name="Signature", blank=True, null=True)
    amount = models.IntegerField(verbose_name="Amount")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)