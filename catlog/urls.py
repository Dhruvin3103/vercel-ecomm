from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MainCateorgyAPI

router = DefaultRouter()
router.register('mainCat', MainCateorgyAPI, 'mainCategory-view')

urlpatterns = [
    path('', include(router.urls))
]