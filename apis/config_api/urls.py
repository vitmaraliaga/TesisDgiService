"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package config_api

Description: urls del api config.
"""

from .views.persona_view import PersonaViewSet
from .views.menu_view import MenuViewSet
from .views.user_view import UserViewSet
from .views.group_view import GroupViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet, base_name='persona')
router.register(r'menus', MenuViewSet, base_name='menu')
router.register(r'users', UserViewSet, base_name='user')
router.register(r'groups', GroupViewSet, base_name='group')

urlpatterns = [
    url(r'^', include(router.urls)),
]
