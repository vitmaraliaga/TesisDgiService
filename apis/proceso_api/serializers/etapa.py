"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package serializer

Description: Serializer del recurso etapa.
"""
from apps.proceso.models.etapa import Etapa
from rest_framework import serializers


class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = ('id', 
                    'nombre', 
                    'descripcion', 
                    'proceso', 
                    'anterior', 
                    'plazo_dias', 
                    'tarea_activador', 
                    'tarea_desactivador', 
                    'orden', 
                    
                    'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)
