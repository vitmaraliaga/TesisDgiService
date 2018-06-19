"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto_api

Description: urls del api proyecto.
"""
from .views.proyecto_view import ProyectoViewSet
from .views.tesista_view import TesistaViewSet
from .views.asesor_view import AsesorViewSet

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'proyectos', ProyectoViewSet, base_name='proyecto')
router.register(r'tesistas', TesistaViewSet, base_name='tesista')
router.register(r'asesores', AsesorViewSet, base_name='asesor')

urlpatterns = [
    url(r'^', include(router.urls)),
]
