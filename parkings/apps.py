from django.apps import AppConfig


class ParkingsConfig(AppConfig):
    name = 'parkings'
    verbose_name = "Vagas"

    def ready(self):
        import parkings.signals