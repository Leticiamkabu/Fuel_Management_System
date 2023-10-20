from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
# from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import *
from fuel_transporter.permissions import *
from django.http import JsonResponse
# Create your views here.

class Registeration_view(APIView):


    def post(self, request):
        serializer = RegisterationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    

class UserView(APIView):

    def get(self, request):
        users = Registeration.objects.all()
        serializer = RegisterationSerializer(users, many=True)

        return Response(serializer.data)


class Login_View(APIView):

    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            token = Token.objects.get(user=user)
            user_details = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'role': user.role,
                # Add other user details you want to include
            }



        # Generate JWT token or session logic here
            return Response({'token': token.key, 'user': user_details },status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class Attendance_View(APIView):

    def post(self, request, action):
        
        permission_classes = (User_priviledge,)
        data = {
            'user': request.user.pk,
            'action': action,
            'clockin': request.data.get('clockin'),  
            'clockout': request.data.get('clockout'), 
        }
        
        serializer = AttendanceSerializer(data = data)
        serializer.is_valid(raise_exception = True)
        serializer.save()  

        return Response(serializer.data)


    def get(self,request,action):
        permission_classes = (Admin_priviledge,)
        queryset = Attendance.objects.all()
        serializer = AttendanceSerializer(queryset, many = True)

        return Response(serializer.data)

    

def get_attendance(request):
    queryset = Attendance.objects.all()
    serializer = AttendanceSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


def list_of_attendance_by_id(request, id):
    queryset = Attendance.objects.filter(user=id)
    serializer = AttendanceSerializer(queryset, many=True)

    return JsonResponse(serializer.data, safe=False)






