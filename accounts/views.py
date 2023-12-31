from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User, Address
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin,ListModelMixin,CreateModelMixin,DestroyModelMixin
from rest_framework.views import APIView
from .serializers import UserSerializer, AddressSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
# from allauth.account.models import EmailAddress
from django.core.mail import send_mail
from django.conf import settings
from uuid import uuid4
from django.contrib.sites.models import Site
from .permisions import IsValidUser
from social_django.models import AbstractUserSocialAuth

def RedirectVerify(request):
    try:
        user_em = AbstractUserSocialAuth.objects.get(uid=request.user.email)
        # print(user_em==None)
        print('hi')
        print(user_em)
        if user_em:
            user = User.objects.get(user=user_em.user)
            user.username=request.user.email
            user.is_email_verified=True
            user.save()
            return redirect("/")
        else : 
            raise Exception("No email found")
    except:
        print('hi')
        raise Exception("Anonymous User")

class Register(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    def get(self, request, id, token):
        try:
            user_obj = User.objects.get(id = id)
            user_data = UserSerializer(user_obj).data
            if(token == user_data['email_token']):
                user_obj.is_email_verified = True
                user_obj.save()
                return redirect('http://127.0.0.1:3000/login')
                # return HttpResponse('<h1>User is Verified Successfully</h1>')
            else:
                return HttpResponse('<h1>Token is not valid</h1>')
        except Exception as e:
            print(e)
            return HttpResponse('<h1>Sorry Some error has occured</h1>')

    def post (self, request):
        try:
            subject = 'Thank You for Regristering proceed to verify'
            serializer = UserSerializer(data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            message = f'Hi!\n{serializer.data["first_name"]}, thank you for registering in our website.\nPlease Click here to verfy Your Account {Site.objects.get_current().domain}accounts/verify/{serializer.data["id"]}/{serializer.data["email_token"]}/\nThis is a Computer generated mail don\'t reply to this mail'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [serializer.data['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            return Response(serializer.data)
        except Exception as e:
            return Response({"Error" : str(e)})

class PasswordResetAPI(APIView):
    def post(self, request):
        try:
            user = User.objects.get(email = request.data.get('email'))
            subject = 'Password Reset Mail'
            uuid = uuid4()
            user.password_reset_token = uuid
            user.save()
            text_content = f'{Site.objects.get_current().domain}accounts/password-reset-redirect/{user.id}/{uuid}/'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, text_content, email_from, recipient_list )
            return Response({'status': 200, 'message' : 'Please check your mail a password reset link has been provided'})
        except Exception as e:
            return Response({'status': 405, 'error': str(e) ,'message': 'Sorry Some error has occured, Please try again after sometime'})

class PasswordResetView(APIView):
    def get(self , request, id, token):
        user_obj = User.objects.get(id=id)
        if(token == user_obj.password_reset_token):
            return render(request, "passwordreset.html", {'id' : id, 'token' : token})
        else:
            return HttpResponse('<h1>Token is not valid</h1>')
    def post(self, request, id, token):
        password = request.POST['password']
        user_obj = User.objects.get(id=id)
        if(token == user_obj.password_reset_token):
            try:
                user_obj.set_password(password)
                user_obj.save()
                return HttpResponse('<h1>User\'s Password changed Successfully</h1>')
            except:
                return HttpResponse('<h1>Some error has occured</h1>')
        else:
            return HttpResponse('<h1>Token is not valid</h1>') 

class UpdateUser(GenericAPIView):
    authentication_classes = [OAuth2Authentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def patch(self, request):
        serializer = self.serializer_class(User.objects.get(id =request.user.id), data = request.data, partial =True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
class Logout(APIView):
    def post (self, request):
        try:
            token = request.data['token']
            instance = Token.objects.get(key = token)
            instance.delete()
            return Response({'message':"logout successfully"})
        except KeyError:
            return Response({'token':['This field is required.']}, status=status.HTTP_400_BAD_REQUEST)

class UserData(APIView):
    authentication_classes = [OAuth2Authentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = UserSerializer(User.objects.get(id = request.user.id))
        return Response(user.data)
    
class AddressAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    authentication_classes = [OAuth2Authentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)

class UpdateAddressAPI(GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    authentication_classes = [OAuth2Authentication,TokenAuthentication]
    permission_classes = [IsAuthenticated, IsValidUser]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    lookup_field = 'id'

    def patch(self, request, id):
        return self.partial_update(request, id)
    def delete(self, request, id):
        return self.destroy(request, id)
    
class ResendVerificationAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post (self, request):
        try:
            subject = 'Thank You for Regristering proceed to verify'
            message = f'Hi!\n{request.user.username}, thank you for registering in Committee Managment System.\nPlease Click here to verfy Your Account {Site.objects.get_current().domain}accounts/verify/{request.user.id}/{request.user.email_token}/\nThis is a Computer generated mail don\'t reply to this mail'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return Response("Email for verification has been send !")
        except Exception as e:
            return Response({"Error":str(e)})