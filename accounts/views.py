from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from rest_framework.generics import GenericAPIView,UpdateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from allauth.account.models import EmailAddress
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def RedirectVerify(request):
    try:
        user_em = EmailAddress.objects.filter(email=request.user.email)
        if user_em:
            user = User.objects.get(email=user_em[0])
            user.is_email_verified=True
            user.save()
            return redirect("/")
        else : 
            raise Exception("No email found")
    except:
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
                return HttpResponse('<h1>User is Verified Successfully</h1>')
            else:
                return HttpResponse('<h1>Token is not valid</h1>')
        except:
            return HttpResponse('<h1>Sorry Some error has occured</h1>')

    def post (self, request):
        try:
            subject = 'Thank You for Regristering proceed to verify'
            serializer = UserSerializer(data = request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            message = f'Hi!\n{serializer.data["username"]}, thank you for registering in Committee Managment System.\nPlease Click here to verfy Your Account http://127.0.0.1:8000/accounts/verify/{serializer.data["id"]}/{serializer.data["email_token"]}/\nThis is a Computer generated mail don\'t reply to this mail'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [serializer.data['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            
            return Response(serializer.data)
        except Exception as e:
            return Response({
                "Error" : str(e)
            })
    
class UpdateUser(GenericAPIView,UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def patch(self, request, id):
        return self.partial_update(request,id)
    
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = UserSerializer(User.objects.get(id = request.user.id))
        return Response(user.data)