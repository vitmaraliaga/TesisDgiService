"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: Serlializer and View del recurso linea_investigacion.
"""
import logging

from apps.academico.models.linea_investigacion import LineaInvestigacion
from rest_framework import viewsets, serializers
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class LineaInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaInvestigacion
        fields = ('id', 'nombre', 'descripcion', 'activo', 'escuela',  'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class LineaInvestigacionViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = LineaInvestigacion.objects.all()
    serializer_class = LineaInvestigacionSerializer