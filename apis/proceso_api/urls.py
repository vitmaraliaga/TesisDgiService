"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package tesis_proceso

Description: urls del api tesis proceso.
"""
from .viewsets.processo import ProcesoViewSet
from .viewsets.etapa import EtapaViewSet
from .viewsets.requisito import RequisitoViewSet
from .viewsets.rol_proceso import RolProcesoViewSet
from .viewsets.resultado import ResultadoViewSet
from .viewsets.tarea import TareaViewSet
from .viewsets.requisito_resultado import RequisitoResultadoViewSet
# from apis.tesis_proceso_api.views.tesis_proceso_view import TesisProcesoViewSet
from apis.tesis_proceso_api.views.tesis_proceso_view import TesisProcesoList

from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'procesos', ProcesoViewSet, base_name='proceso')
router.register(r'etapas', EtapaViewSet, base_name='etapa')
router.register(r'requisitos', RequisitoViewSet, base_name='requisito')
router.register(r'rol-procesos', RolProcesoViewSet, base_name='rol-proceso')
router.register(r'resultados', ResultadoViewSet, base_name='resultado')
router.register(r'tareas', TareaViewSet, base_name='tarea')
router.register(r'requisito-resultados', RequisitoResultadoViewSet, base_name='requisito-resultado')


# tesis_procesos_list = TesisProcesoViewSet.as_view({
    # 'get': 'list_by_proceso',
    # 'post': 'post'
    # 'put': 'update'
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
# }) 

# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'procesos/(?P<proceso_id>.+)/tesis-procesos/$', TesisProcesoList.as_view())
    # url(r'procesos/(?P<proceso_id>.+)/tesis-procesos/$', tesis_procesos_list, name='tesis-proceso-list')

]
