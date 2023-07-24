from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(SizeChart)
admin.site.register(SizeProduct)
admin.site.register(ProdImage)
admin.site.register(ProdReview)
admin.site.register(MainCateorgy)
admin.site.register(SubCateorgy)
admin.site.register(WishlistProduct)

