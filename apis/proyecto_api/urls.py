"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto_api

Description: urls del api proyecto.
"""
from .views.proyecto_view import ProyectoViewSet

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, base_name='proyecto')

urlpatterns = [
    url(r'^', include(router.urls)),
]
