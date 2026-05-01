from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

# A ViewSet para o modelo Customer, que irá lidar com as operações CRUD
# (Create, Read, Update, Delete)
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer