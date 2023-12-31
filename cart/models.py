from django.db import models
from accounts.models import User
from catlog.models import Product,ProductBySize
# Create your models here.

#removed cart model 

# class Cart(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return str(self.user)

class Product_cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)#changed cart to user
    product_by_size = models.ForeignKey(ProductBySize,on_delete=models.CASCADE)
    count = models.IntegerField()
    
    def __str__(self) -> str:
        return str(self.product_by_size) +" "+ str(self.user) +"   "+ str(self.count)