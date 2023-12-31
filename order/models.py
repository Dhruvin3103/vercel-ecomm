from datetime import datetime
from django.db import models

from catlog.models import Product,ProductBySize
from accounts.models import User,Address

# Create your models here.
class Orders(models.Model):
    ORDER_STATUS = [
        ("1", "yet to dispatched"),
        ("2", "Dispatched"),
        ("3", "shipped"),
        ("4", "on the way"),
    ]
    PAY_METHOD = [
        ("1", "Online Payment"),
        ("2", "Cash on delivery")
    ]
    PAYMENT_STATUS = [
        ("1", "paid"),
        ("2", "Not paid")
    ]
    product_by_size = models.ForeignKey(ProductBySize, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    order_status = models.CharField(choices=ORDER_STATUS, max_length=200,default="1")
    payment_type = models.CharField(choices=PAY_METHOD,default="2",max_length=200)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=200, default="2")
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)+" =>  "+str(self.product_by_size)+"=>  "+str(self.address)+" order_id : "+str(self.id)