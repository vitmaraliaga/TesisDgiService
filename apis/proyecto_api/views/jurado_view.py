"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesista.
"""
import logging

from apps.proyecto.models.jurado import Jurado
from apps.config.models.persona import Persona
from rest_framework import viewsets, serializers, filters
from apis.config_api.views.persona_view import PersonaSerializer
from backend_utils.pagination import ModelPagination
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction, IntegrityError

log = logging.getLogger(__name__)


class JuradoSerializer(serializers.ModelSerializer):
    data_persona = PersonaSerializer(source='persona', many=False, read_only=True)
    
    class Meta:
        model = Jurado
        fields = (
            'id', 
            'persona',
            'data_persona',
            'activo',

            'fecha_creacion', 
            'fecha_actualizacion')

        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

class JuradoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Jurado.
    """
    queryset = Jurado.objects.all()
    serializer_class = JuradoSerializer

    
    def create(self, request, *args, **kwargs):
        data = request.data
        data_persona = data.pop('persona')
        try:
            with transaction.atomic():
                try:
                    # Cuando el jurado ya existe.
                    persona_id = data_persona.get('id')
                    model_persona = Persona.objects.get(pk=persona_id)
                    data['persona'] = model_persona.id
                except Exception:
                    # Cuando el jurado es nuevo.
                    persona_id = data_persona.pop('id')
                    persona_serializer = PersonaSerializer(data=data_persona)
                    persona_serializer.is_valid(raise_exception=True)
                    persona_serializer.save()
                    data['persona'] = persona_serializer.data.get('id')
                jurado_serializers = self.get_serializer(data=data)
                jurado_serializers.is_valid(raise_exception=True)
                self.perform_create(jurado_serializers)
        except IntegrityError:
            pass
        headers = self.get_success_headers(jurado_serializers.data)
        return Response(jurado_serializers.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)        
        data_jurado = request.data
        data_persona = data_jurado.pop('persona')
        try:
            with transaction.atomic():
                persona_id = data_persona.get('id')
                model_persona = Persona.objects.get(pk=persona_id)
                persona_serializer = PersonaSerializer(model_persona, data=data_persona, partial=partial)
                persona_serializer.is_valid(raise_exception=True)
                persona_serializer.save()
                
                instance_jurado = self.get_object()
                jurado_serializer = self.get_serializer(instance_jurado, data=data_jurado, partial=partial)
                jurado_serializer.is_valid(raise_exception=True)
                self.perform_update(jurado_serializer)

        except IntegrityError:
            pass

        return Response(jurado_serializer.data)
