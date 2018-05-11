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
# from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class RequisitoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving requisitos.
    """
    # queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer

    def get_queryset(self):
        queryset = Requisito.objects.all()
        tarea_id = self.request.query_params.get('tarea_id', None)
        if tarea_id is not None:
            queryset = queryset.filter(tarea__id = tarea_id)
            print(queryset)
        return queryset
