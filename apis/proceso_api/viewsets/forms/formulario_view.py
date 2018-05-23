"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso formulario.
"""
import logging

from rest_framework import viewsets, mixins, serializers, generics

from apps.proceso.models.forms.formulario import Formulario
from .campo_view import CampoSerializer

log = logging.getLogger(__name__)

class FormularioSerializer(serializers.ModelSerializer):
    # campo_listing = serializers.HyperlinkedIdentityField(view_name='proceso_api:campo-list')
    campos = CampoSerializer(many=True, read_only=True)

    class Meta:
        model = Formulario
        fields = ('id', 'nombre', 'width', 
                'campos',
                'alias', 'descripcion', 'tarea', 'orden', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'campos', 'fecha_creacion', 'fecha_actualizacion')


class FormularioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Formulario.
    """
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer


class FormularioList(generics.ListCreateAPIView):

    serializer_class = FormularioSerializer
    def get_queryset(self):
        tarea_id = self.kwargs['tarea_id']
        if tarea_id is not None:
            return Formulario.objects.filter(tarea__id=tarea_id).order_by('orden')
        else:
            return Formulario.objects.all().order_by('orden')