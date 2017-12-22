"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: Serlializer and View del recurso facultad.
"""
import logging

from apps.academico.models.facultad import Facultad
from rest_framework import viewsets, serializers
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class FacultadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Facultad
        fields = ('id', 'nombre', 'alias', 'activo', 'logo', 
            'tema',
            'mision',
            'vision',
            'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class FacultadViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer