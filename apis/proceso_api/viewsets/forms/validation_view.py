

"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso Validation.
"""
import logging

from rest_framework import viewsets, serializers
from apps.proceso.models.forms.validation import Validation

log = logging.getLogger(__name__)

class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = ('id',
                'nombre',
                'key',
                'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class ValidationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Validation.
    """
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
