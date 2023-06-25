from colorfield.fields import ColorField
from django.db import models
from accounts.models import User
# Create your models here.

class MainCateorgy(models.Model):
    name = models.CharField(max_length=300,null=False)
    image = models.ImageField(upload_to="catlog/")

    def __str__(self) -> str:
        return self.name

class SubCateorgy(models.Model):
    name = models.CharField(max_length=300,null=False)
    main_cateorgy = models.ForeignKey(MainCateorgy,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="catlog/subcatlog")

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    CHOICES = [
        ("S", "small"),
        ("M", "Mdeium"),
        ("L", "Large"),
        ("XL", "Extra large"),
    ]
    name = models.CharField(max_length=300,null=False)
    color = ColorField(default='#FF0000')
    price = models.IntegerField(default=0)
    available_count = models.IntegerField(default=0)
    sub_cateorgy = models.ForeignKey(SubCateorgy,on_delete=models.CharField)
    is_small_size = models.BooleanField(default=False)
    is_medium_size = models.BooleanField(default=False)
    is_large_size = models.BooleanField(default=False)
    is_extra_large_size = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

class ProdImage(models.Model):
    image = models.ImageField(upload_to="catlog/subcatlog/product")
    image_fk = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.image_fk.name +' '+ str(self.id)


class ProdReview(models.Model):
    CHOICES = [
        (1, "Poor"),
        (2, "Satisified"),
        (3, "Good"),
        (4, "Awesome"),
        (5, "Phenominal"),
    ]
    comment = models.CharField(max_length=300,null=True)
    stars = models.IntegerField(choices=CHOICES)
    review_fk = models.ForeignKey(Product,on_delete=models.CASCADE)
    reviewed_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        if self.reviewed_by is not None:
            return self.reviewed_by + "reviewed for " + self.review_fk.name
        else:
            return "Someone reviewed for " + self.review_fk.name