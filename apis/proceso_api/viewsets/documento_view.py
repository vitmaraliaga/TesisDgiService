"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets.forms

Description: ViewSet del recurso CampoValidation.
"""
import logging

from rest_framework import viewsets, serializers
from apps.proceso.models.documento import Documento
from backend_utils.pagination import ModelPagination


log = logging.getLogger(__name__)

class DocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Documento
        fields = ('id',
                'nombre',
                'alias',
                'descripcion',
                'llave_documento',
                'activo',
                'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'data', 'fecha_creacion', 'fecha_actualizacion',)


class DocumentoViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Documento.
    """
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
