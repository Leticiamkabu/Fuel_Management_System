from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import *

# Create your views here.

class Fuel_purchased_details_View(APIView):

    def post(self, request):
        permission_classes = (Fuel_transporter_priviledge,)
        serializer = Fuel_purchased_detailsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)

    def get(self,request):
        permission_classes = (Admin_priviledge)
        queryset = Fuel_purchased_details.objects.latest('date', 'time')
        serializer = Fuel_purchased_detailsSerializer(queryset, many = False)

        return Response(serializer.data)
        

