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
from rest_framework.response import Response
from backend_utils.pagination import ModelPagination 


log = logging.getLogger(__name__)


class AsesorSerializer(serializers.ModelSerializer):
    # persona = PersonaSerializer
    # persona = PersonaSerializer(many=False, read_only=False)
    
    class Meta:
        model = Asesor
        fields = (
            'id', 
            'persona',
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
            model_persona = Persona.objects.get(pk=data_persona.get('id'))
            data['persona'] = '6561e167-9271-492a-a708-af507f6366df'
            print('ya existe!')
            # asesor_serializers = self.get_serializer(data=data)
            # asesor_serializers.is_valid(raise_exception=True)
            # self.perform_create(asesor_serializers)
        except Persona.DoesNotExist:
            print('es nuevo!')
            persona_selializers = PersonaSerializer(data=data_persona)
            persona_selializers.is_valid(raise_exception=True)
            persona_selializers.save()
            data['persona'] = persona_selializers.data.id
        print('ya paso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        asesor_serializers = self.get_serializer(data=data)
        print('ya paso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 2')
        print(data)
        asesor_serializers.is_valid(raise_exception=True)
        print('ya paso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 3')
        self.perform_create(asesor_serializers)
        print('ya paso!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 4')
        headers = self.get_success_headers(asesor_serializers.data)
        return Response(asesor_serializers.data, status=status.HTTP_201_CREATED, headers=headers)