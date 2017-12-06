"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso requisito.
"""
import logging

from ..serializers.requisito import RequisitoSerializer
from apps.proceso.models.requisito import Requisito
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class RequisitoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving requisitos.
    """
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer
