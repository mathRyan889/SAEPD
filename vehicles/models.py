from django.db import models
from customers.models import Customer

class Vehicle_Type(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Tipo de veiculo')
    
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Tipo de Veiculo'
        verbose_name_plural = 'Tipos de Veiculos'
    
    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        Vehicle_Type,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de veiculo'
    )

    license_plate = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Placa'
    )

    brand = models.CharField( #podemos criar uma tabela de marcas e relacionar aqui, mas para simplificar, deixaremos como texto
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Marca'
    )

    model = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Modelo'
    )

    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor'
    )

    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Proprietário'
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.license_plate
