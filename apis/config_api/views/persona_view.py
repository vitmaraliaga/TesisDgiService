"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso persona.
"""
import logging

from apps.config.models.persona import Persona
from rest_framework import viewsets, serializers

log = logging.getLogger(__name__)


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id',
                  'nombres',
                  'apellido_paterno',
                  'apellido_materno',
                  'genero',
                  'fecha_nacimiento',
                  'direccion',
                  'telefono',
                  'celular',
                  'num_doc',
                  'carnet_extrangeria',
                  'foto',

                  'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class PersonaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving personas.
    """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
