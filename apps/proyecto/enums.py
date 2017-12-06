"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto

Description: Enums de la aplicación
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

PROYECTO = 'PROYECTO'
INFORME = 'INFORME'
ETAPAS_CHOICES = (
    (PROYECTO, capfirst(_('proyecto de tesis'))),
    (INFORME, capfirst(_('informe de tesis'))),
)

PROCESO = 'PROCESO'
TERMINADO = 'TERMINADO'
PUBLICADO = 'PUBLICADO'
ABANDONADO = 'ABANDONADO'
OTRO = 'OTRO'
ESTADO_PROYECTO_CHOICES = (
    (PROCESO, capfirst(_('en proceso'))),
    (TERMINADO, capfirst(_('terminado'))),
    (PUBLICADO, capfirst(_('publicado'))),
    (ABANDONADO, capfirst(_('abandonado'))),
    (OTRO, capfirst(_('otro'))),
)

ASESOR = 'ASESOR'
COASESOR = 'COASESOR'
ASESOR1 = 'ASESOR1'
ASESOR2 = 'ASESOR2'
TIPO_ASESOR_CHOICES = (
    (ASESOR, capfirst(_('asesor principal'))),
    (COASESOR, capfirst(_('coasesor'))),
    (ASESOR1, capfirst(_('asesor 1'))),
    (ASESOR2, capfirst(_('asesor 2'))),
)

PRESIDENTE = 'PRESIDENTE'
SECRETARIO = 'SECRETARIO'
OTRO = 'OTRO'
TIPO_JURADO_CHOICES = (
    (PRESIDENTE, capfirst(_('presidente'))),
    (SECRETARIO, capfirst(_('secretario'))),
    (OTRO, capfirst(_('otro'))),
)
