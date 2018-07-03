"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesista.
"""
import logging

from apps.proyecto.models.asesor import Asesor
from apps.config.models.persona import Persona
from rest_framework import viewsets, serializers, filters
from apis.config_api.views.persona_view import PersonaSerializer

from backend_utils.pagination import ModelPagination 


log = logging.getLogger(__name__)


class AsesorSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False, read_only=False)
    
    class Meta:
        model = Asesor
        fields = (
            'id', 
            'persona',
            'activo',

            'fecha_creacion', 
            'fecha_actualizacion')

        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

    def create(self, validated_data):
        persona_data = validated_data.pop('persona')
        # persona = Persona.objects.create(**persona_data)
        persona, created = Persona.objects.update_or_create(
            pk=persona_data.get('id'),
            defaults=persona_data)
        asesor = Asesor.objects.create(persona=persona, **validated_data)
        return asesor

# https://www.reddit.com/r/django/comments/6h6l2f/need_help_with_drf_serializer_validation/
    def update(self, instance, validated_data):
        persona_data = validated_data.get('persona')
        # persona_data = validated_data.pop('persona')
        ipersona = Persona.objects.get(id=instance.persona.id)
        ipersona.nombres = persona_data.get('nombres', ipersona.nombres)
        ipersona.apellido_paterno = persona_data.get('apellido_paterno', ipersona.apellido_paterno)
        ipersona.apellido_materno = persona_data.get('apellido_materno', ipersona.apellido_materno)
        ipersona.genero = persona_data.get('genero', ipersona.genero)
        ipersona.fecha_nacimiento = persona_data.get('fecha_nacimiento', ipersona.fecha_nacimiento)
        ipersona.num_doc = persona_data.get('num_doc', ipersona.num_doc)
        ipersona.save()
        # instance.persona.nombres = persona_data.get('nombres', instance.persona.nombres)
        # instance.persona.apellido_paterno = persona_data.get('apellido_paterno', instance.persona.apellido_paterno)
        # instance.persona.apellido_materno = persona_data.get('apellido_materno', instance.persona.apellido_materno)
        # instance.persona.genero = persona_data.get('genero', instance.persona.genero)
        # instance.persona.fecha_nacimiento = persona_data.get('fecha_nacimiento', instance.persona.fecha_nacimiento)
        # instance.persona.num_doc = persona_data.get('num_doc', instance.persona.num_doc)
        # instance.persona.save()

        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        instance.persona = ipersona
        return instance

class AsesorViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Asesor.
    """
    queryset = Asesor.objects.all()
    serializer_class = AsesorSerializer