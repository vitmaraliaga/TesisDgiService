"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso campo.
"""
import logging

from rest_framework import viewsets, mixins, serializers, generics

from apps.proceso.models.forms.campo import Campo
from .campo_validation_view import CampoValidationSerializer
from .validation_view import ValidationSerializer
log = logging.getLogger(__name__)

class CampoSerializer(serializers.ModelSerializer):
    campovalidation_set = CampoValidationSerializer(many=True, read_only=True)
    # validation = ValidationSerializer(many=True, read_only=True)
    class Meta:
        model = Campo
        fields = ('id',
                'label', 'name', 'type', 'required',
                'width', 'placeholder',
                'model_name',
                'model_pk',
                'model_label',
                'json', 'formulario', 'icon',
                'prefix', 'hint_start', 'hint_end_count_text', 'disabled',
                'multiselect', 'order', 'accept_fileinput', 'multiple_fileinput',
                
                'campovalidation_set',
                # 'validation',
                'tipo_validador',
                'roles_validadores',
                
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