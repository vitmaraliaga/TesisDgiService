"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Tesista.
"""
import logging

from apps.proyecto.models.tesista import Tesista
from apps.config.models.persona import Persona
from rest_framework import viewsets, serializers, filters
from apis.config_api.views.persona_view import PersonaSerializer
from backend_utils.pagination import ModelPagination
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction, IntegrityError

log = logging.getLogger(__name__)


class TesistaSerializer(serializers.ModelSerializer):
    data_persona = PersonaSerializer(
        source='persona', many=False, read_only=True)

    class Meta:
        model = Tesista
        fields = (
            'id',
            'persona',
            'data_persona',
            'activo',

            'fecha_creacion',
            'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class TesistaViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving proyecto.
    """
    queryset = Tesista.objects.all()
    serializer_class = TesistaSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['titulo']

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
                    # Cuando la persona es nueva.
                    persona_id = data_persona.pop('id') # Un arreglo para que el data_persona quede sin su id.
                    persona_serializer = PersonaSerializer(data=data_persona)
                    persona_serializer.is_valid(raise_exception=True)
                    persona_serializer.save()
                    data['persona'] = persona_serializer.data.get('id')
                tesista_serializers = self.get_serializer(data=data)
                tesista_serializers.is_valid(raise_exception=True)
                self.perform_create(tesista_serializers)
        except IntegrityError:
            pass
        headers = self.get_success_headers(tesista_serializers.data)
        return Response(tesista_serializers.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        data_tesista = request.data
        data_persona = data_tesista.pop('persona')
        try:
            with transaction.atomic():
                persona_id = data_persona.get('id')
                model_persona = Persona.objects.get(pk=persona_id)
                persona_serializer = PersonaSerializer(
                    model_persona, data=data_persona, partial=partial)
                persona_serializer.is_valid(raise_exception=True)
                persona_serializer.save()

                instance_tesista = self.get_object()
                tesista_serializer = self.get_serializer(
                    instance_tesista, data=data_tesista, partial=partial)
                tesista_serializer.is_valid(raise_exception=True)
                self.perform_update(tesista_serializer)

        except IntegrityError:
            pass

        return Response(tesista_serializer.data)
