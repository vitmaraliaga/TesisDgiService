"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso requisito.
"""
import logging

from ..serializers.resultado import ResultadoSerializer
from apps.proceso.models.resultado import Resultado
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class ResultadoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Resultado.
    """
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
