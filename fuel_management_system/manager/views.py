from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from fuel_transporter.permissions import *

# Create your views here.

class Fuel_dipping_view(APIView):

    def post(self, request):
        permission_classes = (Manager_priviledge)
        serializer = Fuel_dippingSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    
    def get(self, request):
        dips = Fuel_dipping.objects.all()
        serializer = Fuel_dippingSerializer(dips, many= True)

        return Response(serializer.data)

class Fuel_prices_view(APIView):

    def post(self, request):
        permission_classes = (Manager_priviledge)
        serializer = Fuel_pricesSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)
    
    def get(self, request):
        prices = Fuel_prices.objects.all()
        serializer = Fuel_pricesSerializer(prices, many= True)

        return Response(serializer.data)

class Daily_statistics_view(APIView):

    def get(Self, request):
        queryset = Daily_statistics.objects.all()

        serializer = Daily_statisticsSerializer(data = queryset, many = True)

        return Response(serializer.data)
    