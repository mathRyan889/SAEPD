from rest_framework import serializers
from .models import Vehicle_Type, Vehicle


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Type
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'