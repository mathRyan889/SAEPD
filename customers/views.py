from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

# A ViewSet para o modelo Customer, que irá lidar com as operações CRUD
# (Create, Read, Update, Delete)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]  # Permissões para garantir que apenas usuários autenticados e com privilégios de administrador possam acessar esta ViewSet.

# A IsAdminUser é uma permissão que garante que apenas usuários com privilégios de administrador possam acessar as operações desta ViewSet.
# Isso é importante para proteger os dados dos clientes e garantir que apenas pessoas autorizadas possam manipulá-los.

# O DjangoModelPermissions é uma permissão que verifica as permissões do modelo para as operações de leitura, escrita, atualização e exclusão.
# Ele garante que os usuários tenham as permissões adequadas para realizar essas operações no modelo Customer.
