from rest_framework import serializers
from .models import Customer

# Serializer para o modelo Customer, que irá converter os dados do modelo em formatos como JSON
# e também validar os dados de entrada
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'