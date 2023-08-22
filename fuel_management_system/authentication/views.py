from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
# from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login

# Create your views here.

class Registeration_view(APIView):


    def post(self, request):
        serializer = RegisterationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)

class Login_View(APIView):

     
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # Generate JWT token or session logic here
            return Response({'welcome': 'you are login '},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


