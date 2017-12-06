"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso requisito resultado.
"""
import logging

from ..serializers.requisito_resultado import RequisitoResultadoSerializer
from apps.proceso.models.requisito_resultado import RequisitoResultado
from rest_framework import viewsets, mixins

# from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class RequisitoResultadoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Requisito resultado.
    """
    queryset = RequisitoResultado.objects.all()
    serializer_class = RequisitoResultadoSerializer
