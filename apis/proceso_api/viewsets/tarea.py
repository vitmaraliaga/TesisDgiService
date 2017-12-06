"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso tarea.
"""
import logging

from ..serializers.tarea import TareaSerializer
from apps.proceso.models.tarea import Tarea
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class TareaViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Tarea.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
