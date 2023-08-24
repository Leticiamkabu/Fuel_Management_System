from rest_framework import serializers
from .models import *


class Fuel_purchased_detailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fuel_purchased_details
        fields = [ 'name', 'supplier_name', 'supplier_contact', 'litters_bought','date','time', 'receipt']


    def create(self, validated_data):
        purchase_details = Fuel_purchased_details.objects.create(
            name = validated_data['name'], 
            supplier_name = validated_data['supplier_name'],
            supplier_contact = validated_data['supplier_contact'],
            litters_bought = validated_data['litters_bought'],
            date = validated_data['date'],
            time = validated_data['time'],
            receipt = validated_data['receipt']
        )

        purchase_details.save()

        return purchase_details