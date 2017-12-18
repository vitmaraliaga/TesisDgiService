"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Proyecto.
"""
import logging

from apps.proyecto.models.proyecto import Proyecto
from rest_framework import viewsets, serializers, filters

from backend_utils.pagination import ModelPagination 


log = logging.getLogger(__name__)


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = (
            'id', 
            'titulo', 
            'resumen', 
            'archivo', 
            'fecha_fin',
            'estado',
            'fecha_sustentacion',
            'dictaminador',
            'asesor',
            'jurado',
            'tesista',
            'linea_investigacion',
            'tesis_proceso',

            'fecha_creacion', 
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class ProyectoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving proyecto.
    """
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    filter_backends = (filters.SearchFilter,)
    # filter_fields = ['username', 'email', 'is_staff', 'groups']
    search_fields = ['titulo']