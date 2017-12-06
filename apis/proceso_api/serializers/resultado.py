"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso resultado.
"""
from apps.proceso.models.resultado import Resultado
from rest_framework import serializers


class ResultadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado
        fields = ('id', 'nombre', 'descripcion', 'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
