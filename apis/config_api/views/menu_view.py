"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package viewsets

Description: ViewSet del recurso menu.
"""
import logging

from apps.config.models.menu import Menu
from rest_framework import viewsets, serializers

log = logging.getLogger(__name__)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'titulo', 'descripcion', 'url', 'icono',  'fecha_creacion', 'fecha_actualizacion')
        read_only_fields = ('id', 'fecha_creacion', 'fecha_actualizacion',)


class MenuViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving menus.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
