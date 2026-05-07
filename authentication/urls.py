from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Vão ser usadas as views do Simple JWT para obter, renovar e verificar tokens JWT
urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Endpoint para obter um token JWT (login)
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Endpoint para renovar um token JWT usando um refresh token
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Endpoint para verificar a validade de um token JWT
]
