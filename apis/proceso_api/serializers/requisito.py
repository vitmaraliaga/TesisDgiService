"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso requisito.
"""
from apps.proceso.models.requisito import Requisito
from rest_framework import serializers


class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito
        fields = ('id', 'nombre', 'descripcion', 'activo', 'plazo_dias', 'tipo', 'tarea', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
