from django.db import models
from accounts.models import User
from catlog.models import Product
# Create your models here.

#removed cart model 
class Product_cart(models.Model):
    CHOICES = [
        ("S", "small"),
        ("M", "Mdeium"),
        ("L", "Large"),
        ("XL", "Extra large"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)#changed cart to user
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    size = models.CharField(choices=CHOICES,max_length=300)
    count = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.product)+" "+str(self.size) +" "+ str(self.user) +"   "+ str(self.count)
    

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product_cart)
    cart_price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.user)