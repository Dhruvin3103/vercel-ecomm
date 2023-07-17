from .views import Register, Logout, UserData,UpdateUser,PasswordResetView,PasswordResetAPI,AddressAPI,UpdateAddressAPI,ResendVerificationAPI,RedirectVerify
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('sign-up/', Register.as_view()),
    path('redirect/',RedirectVerify),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('user-data/',UserData.as_view()),
    path('user-data-patch/',UpdateUser.as_view()),
    path('verify/<id>/<token>/', Register.as_view(), name = 'email-verify'),
    path('password-reset/', PasswordResetAPI.as_view(), name = 'password-reset'),
    path('password-reset-redirect/<id>/<token>/', PasswordResetView.as_view(), name = 'password-reset-redirect'),
    path('user-address/', AddressAPI.as_view(), name="user-address"),
    path('user-address/<id>/', UpdateAddressAPI.as_view(), name="user-address-update"),
    path('resend-verification-email/',ResendVerificationAPI.as_view(), name = 'resend-verification-email')
]