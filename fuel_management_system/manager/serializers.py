from rest_framework import serializers
from .models import *

class Fuel_dippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel_dipping
        fields = ['id','name', 'diesel_dipping', 'super_dipping', 'date_time']


    def create(self, validated_data):
        dippings = Fuel_dipping.objects.create(
            name = validated_data['name'],
            diesel_dipping = validated_data['diesel_dipping'],
            super_dipping = validated_data['super_dipping'],

        )
        dippings.save() 

        return dippings

class Fuel_pricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel_prices
        fields = ['user','name','diesel', 'superfuel', 'timestamp']


    def create(self, validated_data):
        prices = Fuel_prices.objects.create(
            name = validated_data['name'],
            diesel = validated_data['diesel'],
            superfuel = validated_data['superfuel'],

        )
        prices.save() 

        return prices

class Daily_statisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_statistics
        fields = ['__all__']

        