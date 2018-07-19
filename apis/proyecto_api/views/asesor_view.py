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
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction, IntegrityError

log = logging.getLogger(__name__)


class AsesorSerializer(serializers.ModelSerializer):
    data_persona = PersonaSerializer(source='persona', many=False, read_only=True)
    
    class Meta:
        model = Asesor
        fields = (
            'id', 
            'persona',
            'data_persona',
            'activo',
            'fecha_creacion', 
            'fecha_actualizacion')

        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

    # def create(self, validated_data):
    #     persona_data = validated_data.pop('persona')
    #     persona, created = Persona.objects.get_or_create(
    #         pk=persona_data.get('id'),
    #         defaults=persona_data)

    #     asesor = Asesor.objects.create(persona=persona, **validated_data)
    #     return asesor

    # # https://www.reddit.com/r/django/comments/6h6l2f/need_help_with_drf_serializer_validation/
    # def update(self, instance, validated_data):
    #     persona_data = validated_data.pop('persona')
    #     instance.persona.nombres = persona_data.get('nombres', instance.persona.nombres)
    #     instance.persona.apellido_paterno = persona_data.get('apellido_paterno', instance.persona.apellido_paterno)
    #     instance.persona.apellido_materno = persona_data.get('apellido_materno', instance.persona.apellido_materno)
    #     instance.persona.genero = persona_data.get('genero', instance.persona.genero)
    #     instance.persona.fecha_nacimiento = persona_data.get('fecha_nacimiento', instance.persona.fecha_nacimiento)
    #     instance.persona.num_doc = persona_data.get('num_doc', instance.persona.num_doc)
    #     instance.persona.save()
    #     instance.activo = validated_data.get('activo', instance.activo)
    #     instance.save()
    #     return instance

class AsesorViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Asesor.
    """
    queryset = Asesor.objects.all()
    serializer_class = AsesorSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data_persona = data.pop('persona')
        try:
            with transaction.atomic():
                try:
                    # Cuando la persona ya existe.
                    persona_id = data_persona.get('id')
                    model_persona = Persona.objects.get(pk=persona_id)
                    data['persona'] = model_persona.id
                except Exception:
                    # Cuando la persona es nuevo.
                    persona_id = data_persona.pop('id')
                    persona_serializer = PersonaSerializer(data=data_persona)
                    persona_serializer.is_valid(raise_exception=True)
                    persona_serializer.save()
                    data['persona'] = persona_serializer.data.get('id')
                asesor_serializers = self.get_serializer(data=data)
                asesor_serializers.is_valid(raise_exception=True)
                self.perform_create(asesor_serializers)
        except IntegrityError:
            pass
        headers = self.get_success_headers(asesor_serializers.data)
        return Response(asesor_serializers.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)        
        data_asesor = request.data
        data_persona = data_asesor.pop('persona')
        try:
            with transaction.atomic():
                persona_id = data_persona.get('id')
                model_persona = Persona.objects.get(pk=persona_id)
                persona_serializer = PersonaSerializer(model_persona, data=data_persona, partial=partial)
                persona_serializer.is_valid(raise_exception=True)
                persona_serializer.save()
                
                instance_asesor = self.get_object()
                asesor_serializer = self.get_serializer(instance_asesor, data=data_asesor, partial=partial)
                asesor_serializer.is_valid(raise_exception=True)
                self.perform_update(asesor_serializer)

        except IntegrityError:
            pass

        return Response(asesor_serializer.data)
