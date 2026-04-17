from django.contrib import admin

from .models import ParkingSpot, ParkingRecord

@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = ['spot_number', 'is_occupied', 'created_at']
    search_fields = ['spot_number']
    list_filter = ['is_occupied']

@admin.register(ParkingRecord)
class ParkingRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle','parkingspot', 'entry_time', 'exit_time', 'created_at']
    search_fields = ['vehicle__license_plate', 'parkingspot__spot_number']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parkingspot" and not request.resolver_match.url_name.endswith('change'):
            kwargs["queryset"] = ParkingSpot.objects.filter(is_occupied=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

        # Sobrescreve o método formfield_for_foreignkey para filtrar as vagas disponíveis apenas na criação de um novo reggistro.
        #  Se o URL da requisição não terminar com 'change', significa que estamos criando um novo registro,
        #  e então filtramos as vagas para mostrar apenas as que estão desocupadas.
