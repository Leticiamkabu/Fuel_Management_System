from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from fuel_transporter.permissions import *
from datetime import datetime
from rest_framework import status

# Create your views here.

class Meter_reading_View(APIView):

    def post(self, request):
        permission_classes = (Fuel_Attendant_priviledge)
        serializer = Meter_readingSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        return Response(serializer.data)

    # update some details of the meter reading form
    def patch(self, request):
        permission_classes = (Fuel_Attendant_priviledge)
        queryset = Meter_reading.objects.get(date = datetime.today().date())
        serializer = Meter_readingSerializer(instance = queryset, data = request.data, partial = True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)


# update all details on the meter reading form
    def patch(self, request):
        permission_classes = (Fuel_Attendant_priviledge)
        queryset = Meter_reading.objects.get(date = datetime.today().date())
        serializer = Meter_readingSerializer(instance = queryset, data = request.data, partial = True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def put(self, request, id):
        permission_classes = (Fuel_Attendant_priviledge)
        try:
            meter_reading = Meter_reading.objects.get(id=id)
        except Meter_reading.DoesNotExist:
            return Response({"error": "Meter reading not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Meter_readingSerializer(meter_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def get(self, request):
        permission_classes = (Fuel_Attendant_priviledge)
        queryset = Meter_reading.objects.latest('date')
        serializer = Meter_readingSerializer(queryset, many = False)

        return Response(serializer.data)

 

    def delete(self, request, id):
        permission_classes = (Fuel_Attendant_priviledge)

        try:
            meter_reading = Meter_reading.objects.get(id=id)
            meter_reading.delete()
        except Meter_reading.DoesNotExist:
            return Response({"error": "Meter reading not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Meter reading deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


    

class Meter_reading_View_by_id(APIView):

    def get(self, request, id):
        permission_classes = (Fuel_Attendant_priviledge)
        queryset = Meter_reading.objects.get(id = id)
        serializer = Meter_readingSerializer(queryset, many = False)

        return Response(serializer.data)