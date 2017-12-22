"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: Serlializer and View del recurso escuela.
"""
import logging

from apps.academico.models.escuela import Escuela
from rest_framework import viewsets, serializers
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)


class EscuelaSerializer(serializers.ModelSerializer):
    
    # facultad = serializers.SlugRelatedField(
        # many=False,
        # read_only=True,
        # slug_field='nombre'
    # )
    facultad_nombre = serializers.SerializerMethodField('is_facultad_nombre')
    
    class Meta:
        model = Escuela
        fields = ('id', 'nombre', 'alias', 'activo', 'logo', 
            'mision',
            'vision',
            'facultad_nombre',
            'facultad',
            'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
    def is_facultad_nombre(self, escuela):
        return escuela.facultad.nombre


class EscuelaViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    serializer_class = EscuelaSerializer