from django.urls import path, include
# Importando o DefaultRouter para criar rotas automaticamente para a ViewSet
from rest_framework.routers import DefaultRouter 
from .views import CustomerViewSet

# Aqui criamos um router e registramos a nossa ViewSet de clientes,
#  o que irá gerar automaticamente as rotas para as operações CRUD
router = DefaultRouter()
router.register('customers', CustomerViewSet)

urlpatterns = [
    # Incluindo as rotas geradas pelo router
    path('', include(router.urls)),
]