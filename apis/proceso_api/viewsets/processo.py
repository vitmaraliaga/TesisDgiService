"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso proceso.
"""
import logging

from django.db.models import Q
from operator import __or__ as OR
from functools import reduce
from ..serializers.processo import ProcesoSerializer
from apps.proceso.models.proceso import Proceso
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class ProcesoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving procesos.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer
    # serializer = ProcesoSerializer(queryset, many=True)
    """
    def get_queryset(self):
        queryset = Proceso.objects.all()
        return queryset

    def list(self, request):
        query = request.query_params.get('query', '')
        all = self.request.query_params.get('all', None)
        if all == 'true':
            self.pagination_class = None
            return Proceso.objects.all()
        if query is not None:
            queryall = (Q(nombre__icontains=query),
                        Q(descripcion__icontains=query))
            queryset = self.get_queryset().filter(reduce(OR, queryall))
            results = self.paginate_queryset(queryset)
        # query1 = self.request.query_params
        # query2 = self.request.query_params.get('all', None)
        # log.info('Este es mi log Hola vimtmar estas queriendo listar')
        # log.info(query)
        # log.info(query1)
        # log.info(query2)
        queryset = Proceso.objects.all()
        serializer = ProcesoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        queryset = Proceso.objects.all()
        proceso = get_object_or_404(queryset, pk=pk)
        serializer = ProcesoSerializer(proceso)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    """