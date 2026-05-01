from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('customers.urls')), # Apontando para as urls do app customers
    path('api/v1/', include('parkings.urls')), # Apontando para as urls do app parkings
    path('api/v1/', include('vehicles.urls')), # Apontando para as urls do app vehicles


    path('admin/', admin.site.urls),
]

