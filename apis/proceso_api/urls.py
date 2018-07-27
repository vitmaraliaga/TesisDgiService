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

#Formulario
from .viewsets.forms.formulario_view import FormularioViewSet
from .viewsets.forms.formulario_view import FormularioList

#Campo
from .viewsets.forms.campo_view import CampoViewSet
from .viewsets.forms.campo_view import CampoList


from .viewsets.forms.campo_validation_view import CampoValidationViewSet
from .viewsets.forms.validation_view import ValidationViewSet


from apis.tesis_proceso_api.views.tesis_proceso_view import TesisProcesoList
from apis.proceso_api.viewsets.tarea import TareaList
from apis.proceso_api.viewsets.model import ModelRestView

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

#Forms
router.register(r'formularios', FormularioViewSet, base_name='formulario')
router.register(r'campos', CampoViewSet, base_name='campo')
router.register(r'campo-validations', CampoValidationViewSet, base_name='campo-validation')
router.register(r'validations', ValidationViewSet, base_name='validation')


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
    url(r'procesos/(?P<proceso_id>.+)/tesis-procesos/$', TesisProcesoList.as_view()),
    url(r'etapas/(?P<etapa_id>.+)/tareas/$', TareaList.as_view()),
    url(r'tareas/(?P<tarea_id>.+)/formularios/$', FormularioList.as_view()),
    url(r'formularios/(?P<formulario_id>.+)/campos/$', CampoList.as_view()),

    url(r'models/$', ModelRestView.as_view(), name='model_rest_view')
    # url(r'procesos/(?P<proceso_id>.+)/tesis-procesos/$', tesis_procesos_list, name='tesis-proceso-list')
]
