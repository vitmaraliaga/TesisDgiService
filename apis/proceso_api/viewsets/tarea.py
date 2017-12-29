"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso tarea.
"""
import logging

from ..serializers.tarea import TareaSerializer
from apps.proceso.models.tarea import Tarea
from rest_framework import viewsets, mixins, generics
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class TareaViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Tarea.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class TareaList(generics.ListCreateAPIView):

    # def get_queryset(self, etapa_id=None):
    serializer_class = TareaSerializer
    def get_queryset(self):
        etapa_id = self.kwargs['etapa_id']
        if etapa_id is not None:
            return Tarea.objects.filter(etapa__id=etapa_id).order_by('orden')
        else:
            return Tarea.objects.all().order_by('orden')

    # def list(self, *args, **kwargs):
        # etapa_id = self.kwargs['etapa_id']
        # if etapa_id is not None:
            # queryset = self.get_queryset(etapa_id)
        # serializer = TareaSerializer(queryset, many=True)
        # return Response(serializer.data)