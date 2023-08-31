from rest_framework import serializers
from .models import *

class Fuel_dippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel_dipping
        fields = ['name', 'diesel_dipping', 'super_dipping', 'date_time']


    def create(self, validated_data):
        dippings = Fuel_dipping.objects.create(
            name = validated_data['name'],
            diesel_dipping = validated_data['diesel_dipping'],
            super_dipping = validated_data['super_dipping'],

        )
        dippings.save() 

        return dippings


class Daily_statisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_statistics
        fields = ['__all__']

        