from rest_framework import serializers
from .models import *

class Meter_readingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter_reading
        fields =['name', 'meter_number','opening_time', 'opening_litter', 'closing_time', 'closing_litter', 'date', 'total_sale']

        def create(self, validated_data):
            readings = Meter_reading.objects.create(
                name = validated_data['name'],
                meter_number = validated_data['meter_number'],
                opening_time = validated_data['opening_time'],
                opening_litter = validated_data['opening_litter'],
                closing_time = validated_data['closing_time'],
                date = validated_data['date'],
                total_sale = validated_data['total_sale']
            )

            readings.save()

            return readings