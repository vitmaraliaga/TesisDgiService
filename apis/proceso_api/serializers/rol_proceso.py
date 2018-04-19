"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso rol proceso.
"""
from apps.proceso.models.rol_proceso import RolProceso
from rest_framework import serializers


class RolProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolProceso
        fields = ('id', 'nombre', 'alias', 'proceso', 'descripcion', 'activo', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
