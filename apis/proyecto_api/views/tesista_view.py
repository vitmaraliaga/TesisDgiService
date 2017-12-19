"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesista.
"""
import logging

from apps.proyecto.models.tesista import Tesista
from rest_framework import viewsets, serializers, filters
from apis.config_api.views.persona_view import PersonaSerializer

from backend_utils.pagination import ModelPagination 


log = logging.getLogger(__name__)


class TesistaSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer
    
    class Meta:
        model = Tesista
        fields = (
            'id', 
            'persona',
            'activo',

            'fecha_creacion', 
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

class TesistaViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving proyecto.
    """
    queryset = Tesista.objects.all()
    serializer_class = TesistaSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['titulo']