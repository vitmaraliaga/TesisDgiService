"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso user.
"""
import logging

from django.contrib.auth.models import User
from rest_framework import viewsets, serializers
from .group_view import GroupSerializer
from apps.config.models.perfil import Perfil
from .persona_view import PersonaSerializer
from .user_view import UserSerializer
from backend_utils.pagination import ModelPagination

log = logging.getLogger(__name__)

class PerfilSerializer(serializers.ModelSerializer):    
    data_usuario = UserSerializer(source='usuario', read_only = True)
    data_persona = PersonaSerializer(source='persona', read_only = True)
    class Meta:
        model = Perfil
        fields = ('url', 'id', 'data_usuario', 'data_persona','usuario', 'persona',)

class PerfilViewSet(ModelPagination, viewsets.ModelViewSet):
    """
    API endpoint that allows perfiles to be viewed or edited.
    """
    queryset = Perfil.objects.all().order_by('-fecha_actualizacion')
    serializer_class = PerfilSerializer
