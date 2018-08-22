"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesis_Etapa.
"""
import logging

from apps.tesis_proceso.models.tesis_tarea import TesisTarea

from rest_framework import viewsets, serializers
from rest_framework.response import Response

from apis.proceso_api.serializers.tarea import TareaSerializer

from apps.proceso.models.tarea import Tarea
from apps.tesis_proceso.models.tesis_etapa import TesisEtapa

log = logging.getLogger(__name__)


class TesisTareaSerializer(serializers.ModelSerializer):
    tesis_tarea_exist = serializers.ReadOnlyField()
    data_tarea = TareaSerializer(many=False, read_only=True)

    class Meta:
        model = TesisTarea
        fields = (
            'id',
            'fecha_inicio',
            'fecha_fin',
            'tesis_etapa',
            'activo',
            'tarea',

            'tesis_tarea_exist',
            'data_tarea',

            'fecha_creacion',
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesisTareaViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving tesis etapa.
    """
    queryset = TesisTarea.objects.all()
    serializer_class = TesisTareaSerializer
    def get_tareas(self, etapa):
        return Tarea.objects.filter(etapa=etapa)

    def list(self, *args):
        etapa = self.request.query_params.get('etapa', None)
        tesis_etapa = self.request.query_params.get('tesis_etapa', None)
        tesisTareas_verificadas = []

        if etapa and tesis_etapa is not None:
            tesisEtapa = TesisEtapa.objects.get(pk=tesis_etapa)
            tareas = self.get_tareas(etapa)
            for tarea in tareas:
                try:
                    tesisTarea = tesisTarea.objects.get(tarea_id = tarea.id, tesis_etapa_id=tesisEtapa.id)
                except tesisTarea.DoesNotExist:
                    tesisTarea = None
                # Apun falta desarrollar esta parte.
                myTesisTarea = TesisTarea(tarea=tarea)
                myTesisTarea.tesis_tarea_exist = tesisTarea
                tesisTareas_verificadas.append(myTesisTarea)
        elif etapa is not None:
            tareas = self.get_tareas(etapa)
            for tarea in tareas:
                # tarea.tesis_proceso= tesiProceso.id
                myTesisTarea = TesisTarea(tarea=tarea)
                myTesisTarea.id = None
                myTesisTarea.fecha_inicio = None
                myTesisTarea.fecha_fin = None
                myTesisTarea.tesis_etapa = None
                myTesisTarea.data_tarea= tarea
                myTesisTarea.tesis_tarea_exist = None
                tesisTareas_verificadas.append(myTesisTarea)
        serializer = TesisTareaSerializer(tesisTareas_verificadas, many=True)
        return Response(serializer.data)