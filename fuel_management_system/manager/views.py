from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from fuel_transporter.permissions import *
from rest_framework import status
from datetime import datetime

# Create your views here.

class Fuel_dipping_view(APIView):

    def post(self, request):
        permission_classes = (Manager_priviledge)
        serializer = Fuel_dippingSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)

    
    def patch(self, request):
        permission_classes = (Manager_priviledge)
        queryset = Fuel_dipping.objects.get(date_time = datetime.today().date())
        serializer = Fuel_dippingSerializer(instance = queryset, data = request.data, partial = True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def put(self, request, id):
        permission_classes = (Manager_priviledge)
        try:
            fuel_dipping_value = Fuel_dipping.objects.get(id=id)
        except fuel_dipping_value.DoesNotExist:
            return Response({"error": "Fuel dipping data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Fuel_dippingSerializer(meter_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    def get(self, request):
        permission_classes = (Manager_priviledge)
        dips = Fuel_dipping.objects.all()
        serializer = Fuel_dippingSerializer(dips, many= True)

        return Response(serializer.data)


    


    def delete(self, request, id):
        permission_classes = (Manager_priviledge)

        try:
            fuel_dipping_value = Fuel_dipping.objects.get(id=id)
            fuel_dipping_value.delete()
        except Attendance.DoesNotExist:
            return Response({"error": "Fuel dipping data not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Fuel dipping data  deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class Fuel_dipping_view_by_id(APIView):

    def get(self, request, id):
        permission_classes = (Manager_priviledge)
        queryset = Fuel_dipping.objects.get(id = id)
        serializer = Fuel_dippingSerializer(queryset, many = False)

        return Response(serializer.data)



class Fuel_prices_view(APIView):

    def post(self, request):
        permission_classes = (Manager_priviledge)
        serializer = Fuel_pricesSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    
    def patch(self, request):
        permission_classes = (Manager_priviledge)
        queryset = Fuel_prices.objects.get(timestamp = datetime.today().date())
        serializer = Fuel_pricesSerializer(instance = queryset, data = request.data, partial = True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    def put(self, request, id):
        permission_classes = (Manager_priviledge)
        try:
            fuel_price = Fuel_prices.objects.get(id=id)
        except Fuel_prices.DoesNotExist:
            return Response({"error": "Fuel price data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Fuel_pricesSerializer(meter_reading, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def get(self, request):
        permission_classes = (Manager_priviledge)
        prices = Fuel_prices.objects.all()
        serializer = Fuel_pricesSerializer(prices, many= True)

        return Response(serializer.data)

   

    def delete(self, request, id):
        permission_classes = (Manager_priviledge)

        try:
            fuel_prices = Fuel_prices.objects.get(id=id)
            fuel_prices.delete()
        except Fuel_prices.DoesNotExist:
            return Response({"error": "Fuel price data  not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Fuel price data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



class Fuel_prices_view_by_id(APIView):

    def get(self, request, id):
        permission_classes = (Manager_priviledge)
        queryset = Fuel_prices.objects.get(id = id)
        serializer = Fuel_pricesSerializer(queryset, many = False)

        return Response(serializer.data)


class Daily_statistics_view(APIView):

    def get(Self, request):
        queryset = Daily_statistics.objects.all()

        serializer = Daily_statisticsSerializer(data = queryset, many = True)

        return Response(serializer.data)
    