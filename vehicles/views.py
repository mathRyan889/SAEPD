from rest_framework import viewsets
from core.permissions import IsOwnerOfVehicleOrRecord
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Vehicle_Type, Vehicle
from .serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = Vehicle_Type.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    # A IsAdminUser vai garantir que apenas usuários administradores possam criar, atualizar ou deletar tipos de veículos, enquanto outros usuários autenticados poderão apenas ler os dados.


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]


def get_queryset(self):
    user = self.request.user
    if user.is_staff:
        return Vehicle.objects.all()
    return Vehicle.objects.filter(owner__user=user)
    # O método get_queryset é sobrescrito para garantir que os usuários comuns só possam acessar
    # os veículos que possuem, enquanto os administradores podem acessar todos os veículos.
