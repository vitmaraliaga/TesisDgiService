"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso proceso.
"""
from apps.proceso.models.proceso import Proceso
from rest_framework import serializers


class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proceso
        fields = ('id', 'nombre', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion')
    """
    def create(self, validated_data):
        proceso_data = validated_data.pop()
    """