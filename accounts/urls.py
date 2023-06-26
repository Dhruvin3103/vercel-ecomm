from .views import Register, Logout, UserData, RedirectVerify,UpdateUser,PasswordResetView,PasswordResetAPI
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('sign-up/', Register.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('user-data/',UserData.as_view()),
    path('redirect/',RedirectVerify),
    path('user-data/<id>/',UpdateUser.as_view()),
    path('verify/<id>/<token>/', Register.as_view(), name = 'email-verify'),
    path('password-reset/', PasswordResetAPI.as_view(), name = 'password-reset'),
    path('password-reset-redirect/<id>/<token>/', PasswordResetView.as_view(), name = 'password-reset-redirect'),
]