"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico_api

Description: urls del api académico.
"""

from .views.linea_investigacion_view import LineaInvestigacionViewSet
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'linea-investigacions', LineaInvestigacionViewSet, base_name='linea-investigacion')


urlpatterns = [
    url(r'^', include(router.urls)),
]
