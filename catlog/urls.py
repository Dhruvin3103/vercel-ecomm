from django.urls import path, include
from .views import MainCateorgyAPI, ProductAPI, SubCateorgyAPI, WishlistProductAPI

urlpatterns = [
    path('main-cat/', MainCateorgyAPI.as_view(), name = 'mainCategory-view'),
    path('sub-cat/<int:main_cat_id>/', SubCateorgyAPI.as_view(), name = 'subCategory-view'),
    path('product/<int:sub_cat_id>/', ProductAPI.as_view(), name = 'product-view'),
    path('wishlist/', WishlistProductAPI.as_view(), name = 'Whislist-post-view'),
]