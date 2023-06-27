from django.db import models
from accounts.models import User
from catlog.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)

class Product_cart(models.Model):
    CHOICES = [
        ("S", "small"),
        ("M", "Mdeium"),
        ("L", "Large"),
        ("XL", "Extra large"),
    ]
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(choices=CHOICES,max_length=300)
    count = models.IntegerField()