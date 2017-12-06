"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package tesis_proceso_api

Description: urls del api tesis_proceso.
"""
from .views.tesis_proceso_view import TesisProcesoViewSet
from .views.tesis_etapa_view import TesisEtapaViewSet

from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()

tesis_procesos_list = TesisProcesoViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

tesis_etapa_list = TesisEtapaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
tesis_etapa_detail = TesisEtapaViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# router.register(r'tesis-procesos', TesisProcesoViewSet, base_name='tesis-proceso')
# router.register(r'tesis-etapas', TesisEtapaViewSet, base_name='tesis-etapa')


urlpatterns = format_suffix_patterns([
    # url(r'^', include(router.urls)),
    url(r'^tesis-etapas/$', tesis_etapa_list, name='tesis-etapa-list'),
    url(r'^tesis-etapas/(?P<pk>[0-9]+)/$', tesis_etapa_detail, name='tesis-etapa-detail'),
    url(r'^tesis-procesos/$', tesis_procesos_list, name='tesis-proceso-list')

])
