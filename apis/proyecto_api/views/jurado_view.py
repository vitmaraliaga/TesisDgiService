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

log = logging.getLogger(__name__)


class JuradoSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False, read_only=False)
    
    class Meta:
        model = Jurado
        fields = (
            'id', 
            'persona',
            'activo',

            'fecha_creacion', 
            'fecha_actualizacion')

        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

    def create(self, validated_data):
        persona_data = validated_data.pop('persona')
        persona, created = Persona.objects.update_or_create(
            pk=persona_data.get('id'),
            defaults=persona_data)
        jurado = Jurado.objects.create(persona=persona, **validated_data)
        return jurado

    def update(self, instance, validated_data):
        persona_data = validated_data.pop('persona')
        instance.persona.nombres = persona_data.get('nombres', instance.persona.nombres)
        instance.persona.apellido_paterno = persona_data.get('apellido_paterno', instance.persona.apellido_paterno)
        instance.persona.apellido_materno = persona_data.get('apellido_materno', instance.persona.apellido_materno)
        instance.persona.genero = persona_data.get('genero', instance.persona.genero)
        instance.persona.fecha_nacimiento = persona_data.get('fecha_nacimiento', instance.persona.fecha_nacimiento)
        instance.persona.num_doc = persona_data.get('num_doc', instance.persona.num_doc)
        instance.persona.save()

        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance

class JuradoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Jurado.
    """
    queryset = Jurado.objects.all()
    serializer_class = JuradoSerializer