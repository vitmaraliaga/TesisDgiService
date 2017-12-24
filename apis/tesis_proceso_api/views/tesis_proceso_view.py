"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso tesis-proceso.
"""
import logging

from django.http import Http404
from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from apps.proyecto.models.proyecto import Proyecto
from apis.proceso_api.serializers.processo import ProcesoSerializer
from apis.proyecto_api.views.proyecto_view import ProyectoSerializer
from rest_framework import viewsets, mixins, serializers, generics, views, status
from rest_framework.response import Response

from backend_utils.pagination import ModelPagination

import datetime

log = logging.getLogger(__name__)


class TesisProcesoSerializer(serializers.ModelSerializer):
    proceso = ProcesoSerializer
    # proceso = ProcesoSerializer(many=False, read_only=True)
    # proceso = serializers.SlugRelatedField(
        # many=False,
        # read_only=True,
        # slug_field='id'
    # )

    proyecto = serializers.SlugRelatedField(
        # many=False,
        read_only=True,
        slug_field='titulo'
    )
    
    class Meta:
        model = TesisProceso
        fields = ('id', 'fecha_inicio', 'fecha_fin', 'estado',
                  'proceso',
                  'proyecto',
                  'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesisProcesoViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = TesisProceso.objects.all()
    serializer_class = TesisProcesoSerializer


class TesisProcesoList(generics.ListCreateAPIView):
    """
    List all tesis procesos, or create a new Tesis proceso
    """
    serializer_class = TesisProcesoSerializer
    def get_queryset(self, proceso_id=None):
        if proceso_id is not None:
            return TesisProceso.objects.filter(proceso__id=proceso_id)
        else:
            return TesisProceso.objects.all()

    # Este list es de list create del generics
    def list(self, *args, **kwargs):
        proceso_id = self.kwargs['proceso_id']
        queryset = self.get_queryset(proceso_id)
        serializer = TesisProcesoSerializer(queryset, many=True)
        return Response(serializer.data)

    # Este create es del mixins
    def create(self, request, *args, **kwargs):

        # if not request.data._mutable:
            # request.data._mutable = True

        # insert Proceso
        request.data['fecha_inicio'] = datetime.datetime.now()
        request.data['estado'] = 'ACTIVO'
        serializer = TesisProcesoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # insert proyecto
        data_proyecto = {
            'id': None,
            'titulo': request.data['proyecto_titulo'],
            'resumen': None,
            'archivo': None,
            'fecha_fin': None,
            'estado': 'PROCESO',
            'fecha_sustentacion': None,
            'dictaminador': [],
            'asesor': [],
            'jurado': [],
            'tesista': ['852b5d9e-6bbe-4661-8d68-1e978b7a9dcd'], # Tesista key
            'linea_investigacion': ['d33d6948-3650-496b-abb7-6970e93fe614'],  # Linea_investigacion key
            'tesis_proceso': serializer.data['id']
            }
        serializer1 = ProyectoSerializer(data = data_proyecto)
        serializer1.is_valid(raise_exception=True)
        serializer1.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TesisProcesoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a tesis proceso instance.
    """
    queryset = TesisProceso.objects.all()
    serializer_class = TesisProcesoSerializer
    
#    def get_object(self, pk):
#        try:
#            return TesisProceso.objects.get(pk=pk)
#        except TesisProceso.DoesNotExist:
#            raise Http404

#    def get(self, request, pk, format=None):
#        tesis_proceso = self.get_object(pk)
#        tesis_proceso = TesisProcesoSerializer(tesis_proceso)
#        return Response(tesis_proceso.data)

#    def put(self, request, pk, format=None):
#        tesis_proceso = self.get_object(pk)
#        serializer = TesisProcesoSerializer(tesis_proceso, data=request.DATA)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#    def delete(self, request, pk, format=None):
#        tesis_proceso = self.get_object(pk)
#        tesis_proceso.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

# class TesisProcesoViewSet(views.APIView):
#     """
#     A simple ViewSet for listing or retrieving TesisProceso.
#     """
#     # serializer_class = TesisProcesoSerializer
#     def get_queryset(self, proceso_id=None):
#         if proceso_id is not None:
#             return TesisProceso.objects.filter(proceso__id=proceso_id)
#         else:
#             return TesisProceso.objects.all()                

#     def get(self, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = TesisProcesoSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def list_by_proceso(self, *args, **kwargs):
#         proceso_id = self.kwargs['proceso_id']
#         queryset = self.get_queryset(proceso_id)
#         serializer = TesisProcesoSerializer(queryset, many=True)
#         return Response(serializer.data)

#     # def perform_create(self, serializer):
#         # serializer.save()

#     def post(self, request, *args, **kwargs):
#         data = request.data
#         print('data>>>>>>>>>>>>>>>>>>>>>><<<')
#         print(data)
#         data['fecha_inicio'] = datetime.datetime.now().isoformat()
#         data['estado'] = 'ACTIVO'
#         print('data>>>>>>>>>>>>>>>>>>>>>><<<')
#         print(data)

#         # print(data['proceso_id'])
#         # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

#         # TesisProceso.objects.create(
#             # fecha_inicio = datetime.datetime.now, 
#             # fecha_fin = datetime.datetime.now, 
#             # estado = 'ACTIVO',
#             # proceso_id = data['proceso_id']
#             # )
#         serializer = self.get_serializer(data=request.data)
#         print(serializer)
#         print('serializer')

#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)    
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializers.data, status=status.HTTP_201_CREATED, headers=headers)
#     # def retrieve(self, request, pk=None):
#     #     queryset = User.objects.all()
#     #     user = get_object_or_404(queryset, pk=pk)
#     #     serializer = UserSerializer(user)
#     #     return Response(serializer.data)
