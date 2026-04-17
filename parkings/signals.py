from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ParkingRecord

@receiver(post_save, sender=ParkingRecord)
def update_parking_spot_status(sender, instance, created, **kwargs):
    parking_spot = instance.parkingspot #vai buscar a vaga associada ao registro de estacionamento
    parking_spot.is_occupied = instance.exit_time is None #se exit_time for None, a vaga está ocupada; caso contrário, está livre
    parking_spot.save()