from django.shortcuts import render
from .models import User
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from allauth.account.models import EmailAddress
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
    def post (self, request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = UserSerializer(User.objects.get(id = request.user.id))
        return Response(user.data)