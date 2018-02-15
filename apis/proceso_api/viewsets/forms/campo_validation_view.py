"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso CampoValidation.
"""
import logging

from rest_framework import viewsets, serializers
from apps.proceso.models.forms.campo_validation import CampoValidation
from .validation_view import ValidationSerializer

log = logging.getLogger(__name__)

class CampoValidationSerializer(serializers.ModelSerializer):
    # validation = ValidationSerializer(many=False, read_only=True)
    validation = serializers.SlugRelatedField(read_only=True, slug_field='key')
    # campo = serializers.SlugRelatedField(read_only=True, slug_field='key')
    class Meta:
        model = CampoValidation
        fields = ('id',
                'data',
                # 'campo', 
                'validation', 
                'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'data', 'fecha_creacion', 'fecha_actualizacion',)


class CampoValidationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving CampoValidation.
    """
    queryset = CampoValidation.objects.all()
    serializer_class = CampoValidationSerializer
