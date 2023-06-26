from .views import Register, Logout, UserData, RedirectVerify,UpdateUser
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('sign-up/', Register.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('user-data/',UserData.as_view()),
    path('redirect/',RedirectVerify),
    path('user-data/<id>/',UpdateUser.as_view())
]