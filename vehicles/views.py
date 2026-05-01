from rest_framework import viewsets
from .models import Vehicle_Type, Vehicle
from .serializers import VehicleTypeSerializer, VehicleSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = Vehicle_Type.objects.all()
    serializer_class = VehicleTypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer