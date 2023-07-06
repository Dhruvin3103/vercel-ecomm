from django.db import models

from catlog.models import Product
from accounts.models import User,Address

# Create your models here.

class Orders(models.Model):
    CHOICES = [
        ("1", "Dispatched"),
        ("2", "shipped"),
        ("3", "on the way"),
    ]
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
    status = models.CharField(choices=CHOICES,max_length=200)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
