from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import *
from rest_framework import status
from datetime import datetime
# Create your views here.

class Fuel_purchased_details_View(APIView):

    def post(self, request):
        permission_classes = (Fuel_transporter_priviledge,)
        serializer = Fuel_purchased_detailsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, id):
        permission_classes = (Fuel_transporter_priviledge,)
        try:
            fuel_purchase = Fuel_purchased_details.objects.get(id=id)
        except fuel_purchase.DoesNotExist:
            return Response({"error": "Fuel purchase data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Fuel_purchased_detailsSerializer(fuel_purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

    def get(self,request):
        permission_classes = (Admin_priviledge,Fuel_transporter_priviledge)
        queryset = Fuel_purchased_details.objects.latest('date', 'time')
        serializer = Fuel_purchased_detailsSerializer(queryset, many = False)

        return Response(serializer.data)

    def get(self, request, id):
        permission_classes = (Admin_priviledge,Fuel_transporter_priviledge)
        queryset = Fuel_purchased_details.objects.get(id = id)
        serializer = Fuel_purchased_detailsSerializer(queryset, many = False)

        return Response(serializer.data)


    def delete(self, request, id):
        permission_classes = (Admin_priviledge,Fuel_transporter_priviledge)

        try:
            fuel_purchase = Fuel_purchased_details.objects.get(id=id)
            fuel_purchase.delete()
        except Fuel_purchased_details.DoesNotExist:
            return Response({"error": "Fuel purchase data not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Fuel purchase data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        

