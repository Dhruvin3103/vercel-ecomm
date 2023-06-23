from .views import Register, Logout, UserData
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('sign-up/', Register.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('user-data/',UserData.as_view())
]