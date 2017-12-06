"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso etapa.
"""
import logging

from ..serializers.etapa import EtapaSerializer
from apps.proceso.models.etapa import Etapa
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class EtapaViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving etapas.
    """
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer
