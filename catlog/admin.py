from django.contrib import admin
from .models import Product,ProdImage,ProdReview,MainCateorgy,SubCateorgy,Whishlist
# Register your models here.
admin.site.register(Product)
admin.site.register(ProdImage)
admin.site.register(ProdReview)
admin.site.register(MainCateorgy)
admin.site.register(SubCateorgy)
admin.site.register(Whishlist)
