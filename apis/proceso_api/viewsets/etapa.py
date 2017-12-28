"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso etapa.
"""
import logging

from ..serializers.etapa import EtapaSerializer
from apps.proceso.models.etapa import Etapa
from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


# class EtapaViewSet(ModelPagination, viewsets.ModelViewSet):
class EtapaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving etapas.
    """
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

    def filter_queryset(self, queryset):
        tesis_proceso_id = self.request.query_params.get('tesis_proceso_id', None)
        proceso_id = None

        if tesis_proceso_id is not None:
            proceso_id = TesisProceso.objects.get(pk=tesis_proceso_id).proceso_id
        
        if proceso_id is not None:
            queryset = queryset.filter(proceso_id=proceso_id).order_by('orden')
        
        return queryset