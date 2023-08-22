from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegisterationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registeration
        fields = ['first_name', 'last_name', 'email', 'role', 'phone_number', 'password']

    def create(self, validated_data):

        user_registeration = Registeration.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            role = validated_data['role'],
            phone_number = validated_data['phone_number'],
            
        )

        user_registeration.set_password(validated_data['password'])
        user_registeration.save()
        
        
        return user_registeration


