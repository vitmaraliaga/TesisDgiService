"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesis_Etapa.
"""
import logging

from apps.tesis_proceso.models.tesis_etapa import TesisEtapa
from rest_framework import viewsets, serializers

log = logging.getLogger(__name__)


class TesisEtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TesisEtapa
        fields = (
            'id', 'fecha_inicio', 'fecha_fin', 'activo', 'tesis_proceso', 'etapa', 'fecha_creacion',
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesisEtapaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving tesis etapa.
    """
    queryset = TesisEtapa.objects.all()
    serializer_class = TesisEtapaSerializer
