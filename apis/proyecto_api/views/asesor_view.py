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
        extra_kwargs = {
        'id': {
            'read_only': False, 
            'required': True
            }
        } #very important
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)

    def create(self, validated_data):
        # persona_data = validated_data.pop('persona')
        # asesor = Asesor.objects.create(**validated_data)
        # Persona.objects.create(asesor=asesor, **persona_data)
        # return asesor
        persona_data = validated_data.pop('persona')
        persona = Persona.objects.create(**persona_data)
        asesor = Asesor.objects.create(persona=persona, **validated_data)
        return asesor

    def update(self, instance, validated_data):
        instance.persona = validated_data['persona']
        instance.save()

        # Delete any detail not included in the request
        asesor_ids = [item['asesor_id'] for item in validated_data['asesors']]
        for asesor in persona.asesors.all():
            if asesor.id not in asesor_ids:
                asesor.delete()

        # Create or update owner 
        for asesor in validated_data['asesors']:
            asesorObj = Asesor.objects.get(pk=item['id'])
            if asesorObje:
                asesorObj.persona=item['persona']
                ....fields...
            else:
               asesorObj = Asesor.create(car=instance,**owner)
            ownerObj.save()

        return instance


class AsesorViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Asesor.
    """
    queryset = Asesor.objects.all()
    serializer_class = AsesorSerializer