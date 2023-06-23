from colorfield.fields import ColorField
from django.db import models

# Create your models here.

class MainCateorgy(models.Model):
    name = models.CharField(max_length=300,null=False)
    image = models.ImageField(upload_to="catlog/")



class SubCateorgy(models.Model):
    name = models.CharField(max_length=300,null=False)
    MainCateorgy = models.ForeignKey(MainCateorgy,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="catlog/subcatlog")


class Products(models.Model):
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
    SubCateorgy = models.ForeignKey(SubCateorgy,on_delete=models.CharField)
    is_small_size = models.BooleanField(default=False)
    is_medium_size = models.BooleanField(default=False)
    is_large_size = models.BooleanField(default=False)
    is_extra_large_size = models.BooleanField(default=False)

class ProdImages(models.Model):
    image = models.ImageField(upload_to="catlog/subcatlog/product")
    image_fk = models.ForeignKey(Products,on_delete=models.CASCADE)


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
    review_fk = models.ForeignKey(Products,on_delete=models.CASCADE)