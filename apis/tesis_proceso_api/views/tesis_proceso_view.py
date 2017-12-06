"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso tesis-proceso.
"""
import logging

from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from apis.proceso_api.serializers.processo import ProcesoSerializer
from rest_framework import viewsets, mixins, serializers, generics, views
from rest_framework.response import Response
from backend_utils.pagination import ModelPagination
import datetime

log = logging.getLogger(__name__)

class TesisProcesoSerializer(serializers.ModelSerializer):
    # proceso = ProcesoSerializer

    class Meta:
        model = TesisProceso
        fields = ('id', 'fecha_inicio', 'fecha_fin', 'estado', 
        # 'proceso_id', 
        'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesisProcesoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving TesisProceso.
    """
    serializer_class = TesisProcesoSerializer
    def get_queryset(self, proceso_id=None):
        if proceso_id is not None:
            return TesisProceso.objects.filter(proceso__id=proceso_id)
        else:
            return TesisProceso.objects.all()                
    
    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TesisProcesoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def list_by_proceso(self, *args, **kwargs):
        proceso_id = self.kwargs['proceso_id']
        queryset = self.get_queryset(proceso_id)
        serializer = TesisProcesoSerializer(queryset, many=True)
        return Response(serializer.data)
        
    # def perform_create(self, serializer):
        # serializer.save()

    def create(self, request, *args, **kwargs):
        data = request.data
        print('data>>>>>>>>>>>>>>>>>>>>>><<<')
        print(data)
        data['fecha_inicio'] = datetime.datetime.now().isoformat()
        data['estado'] = 'ACTIVO'
        print('data>>>>>>>>>>>>>>>>>>>>>><<<')
        print(data)

        # print(data['proceso_id'])
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        # TesisProceso.objects.create(
            # fecha_inicio = datetime.datetime.now, 
            # fecha_fin = datetime.datetime.now, 
            # estado = 'ACTIVO',
            # proceso_id = data['proceso_id']
            # )
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        print('serializer')
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)    
        headers = self.get_success_headers(serializer.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED, headers=headers)
    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    