"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package views

Description: View del recurso Group.
"""
import logging

from django.contrib.auth.models import Group
from rest_framework import viewsets, serializers

log = logging.getLogger(__name__)

class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('id', 'name',)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer