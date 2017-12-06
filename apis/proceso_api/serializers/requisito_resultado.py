"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso requisito resultado.
"""
from apps.proceso.models.requisito_resultado import RequisitoResultado
from rest_framework import serializers


class RequisitoResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitoResultado
        fields = ('id', 'activo', 'requisito', 'resultado', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
