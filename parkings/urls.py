from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkingRecordViewSet, ParkingSpotViewSet

router = DefaultRouter()
router.register('parkings/records', ParkingRecordViewSet)
router.register('parkings/spots', ParkingSpotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]