"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso campo.
"""
import logging

from rest_framework import viewsets, mixins, serializers, generics

from apps.proceso.models.forms.campo import Campo

log = logging.getLogger(__name__)

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo
        fields = ('id', 
                'label', 'key', 'type', 'required', 
                'flex', 'min', 'max', 'backgroud', 
                'model', 'json', 'formulario', 'icon', 
                'prefix', 'hint_start', 'hint_end_count_text', 'disabled', 
                'multiselect', 'order', 
                
                
                'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class CampoViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Campo.
    """
    queryset = Campo.objects.all()
    serializer_class = CampoSerializer


class CampoList(generics.ListCreateAPIView):

    serializer_class = CampoSerializer
    def get_queryset(self):
        formulario_id = self.kwargs['formulario_id']
        if formulario_id is not None:
            return Campo.objects.filter(formulario__id=formulario_id).order_by('order')
        else:
            return Campo.objects.all().order_by('order')