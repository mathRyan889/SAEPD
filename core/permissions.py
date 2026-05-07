from rest_framework import permissions


class IsOwnerOfVehicleOrRecord(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user
        # Verifica se o objeto tem um atributo 'owner' e se o usuário associado a esse proprietário
        #  é o mesmo que o usuário da requisição.

        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.owner.user == user
        # Verifica se o objeto tem um atributo 'vehicle' e se esse veículo tem um proprietário,
        #  e se o usuário associado a esse proprietário é o mesmo que o usuário da requisição.

        return False

    # Basicamente, essa permissão personalizada verifica se o usuário autenticado é o
    # proprietário do veículo ou do registro de estacionamento.
    #  Se o objeto tiver um atributo 'owner', ele verifica se o usuário associado a esse proprietário é o mesmo que o usuário da requisição.
    #  Se o objeto tiver um atributo 'vehicle' e esse veículo tiver um proprietário,
    #  ele verifica se o usuário associado a esse proprietário é o mesmo que o usuário da requisição.
    #  Se nenhuma dessas condições for atendida, a permissão é negada.
