from django.contrib import admin
from .models import Products,ProdImages,ProdReview,MainCateorgy,SubCateorgy
# Register your models here.
admin.site.register(Products)
admin.site.register(ProdImages)
admin.site.register(ProdReview)
admin.site.register(MainCateorgy)
admin.site.register(SubCateorgy)
