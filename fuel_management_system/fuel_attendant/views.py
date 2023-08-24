from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from fuel_transporter.permissions import *
from datetime import datetime

# Create your views here.

class Meter_reading_View(APIView):

    def post(self, request):
        # permission_classes = (Fuel_Attendant_priviledge)
        serializer = Meter_readingSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()

        return Response(serializer.data)


    def patch(self, request):

        queryset = Meter_reading.objects.get(date = datetime.today().date())
        serializer = Meter_readingSerializer(instance = queryset, data = request.data, partial = True)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)
