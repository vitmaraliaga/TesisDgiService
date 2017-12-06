"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso requisito.
"""
import logging

from ..serializers.rol_proceso import RolProcesoSerializer
from apps.proceso.models.rol_proceso import RolProceso
from rest_framework import viewsets, mixins
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class RolProcesoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Rol proceso.
    """
    queryset = RolProceso.objects.all()
    serializer_class = RolProcesoSerializer
