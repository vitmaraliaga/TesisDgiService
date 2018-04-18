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

log = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):    
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'is_staff', 'groups',)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer