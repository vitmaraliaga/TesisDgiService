"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesis_Etapa.
"""
import logging

from apps.tesis_proceso.models.tesis_etapa import TesisEtapa

from rest_framework import viewsets, serializers
from rest_framework.response import Response

from apis.proceso_api.serializers.etapa import EtapaSerializer

from apps.proceso.models.etapa import Etapa
from apps.tesis_proceso.models.tesis_proceso import TesisProceso

log = logging.getLogger(__name__)


class TesisEtapaSerializer(serializers.ModelSerializer):
    has_made = serializers.ReadOnlyField()
    class Meta:
        model = TesisEtapa
        fields = (
            'id', 'fecha_inicio', 'has_made', 'fecha_fin', 'activo', 'tesis_proceso', 'etapa', 'fecha_creacion',
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesisEtapaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving tesis etapa.
    """
    queryset = TesisEtapa.objects.all()
    serializer_class = TesisEtapaSerializer
    def get_etapas(self, proceso):
        return Etapa.objects.filter(proceso=proceso)

    def list(self, *args):
        tesis_proceso = self.request.query_params.get('tesis_proceso', None)
        tesisEtapas_verificadas = []

        if tesis_proceso is not None:
            tesiProceso = TesisProceso.objects.get(pk=tesis_proceso)
            etapas = self.get_etapas(tesiProceso.proceso.id)
            for etapa in etapas:
                # Comprovar si esta etapa esta registrada en tesis etapa
                tesisEtapa = TesisEtapa.objects.filter(etapa_id = etapa.id, tesis_proceso_id=tesiProceso.id)
                # Convertimos esta etapa en tesisEtapa
                etapa.tesis_proceso= tesiProceso.id
                etapa.etapa= etapa.id
                etapa.has_made = tesisEtapa # Aquí me quedé
                tesisEtapas_verificadas.append(etapa)
                
        serializer = TesisEtapaSerializer(tesisEtapas_verificadas, many=True)
        return Response(serializer.data)