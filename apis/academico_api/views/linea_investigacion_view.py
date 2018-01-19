"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: Serlializer and View del recurso linea_investigacion.
"""
import logging

from apps.academico.models.linea_investigacion import LineaInvestigacion
from apis.academico_api.views.escuela_view import EscuelaSerializer
from rest_framework import viewsets, serializers
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class LineaInvestigacionSerializer(serializers.ModelSerializer):
    escuela_nombre = serializers.SerializerMethodField('is_escuela_nombre')

    class Meta:
        model = LineaInvestigacion
        fields = ('id', 'nombre',
                  'descripcion', 'activo', 'escuela_nombre',
                  'escuela', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id',
                            'escuela_nombre',
                            'fecha_creacion', 'fecha_actualizacion',)

    def is_escuela_nombre(self, lineaInvestigacion):
        return lineaInvestigacion.escuela.nombre


class LineaInvestigacionViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = LineaInvestigacion.objects.all()
    serializer_class = LineaInvestigacionSerializer
