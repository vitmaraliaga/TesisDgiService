"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package tesis_proceso

Description: Enums de la aplicación
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

ACTIVO = 'ACTIVO'
TERMINADO = 'TERMINADO'
ABANDONADO = 'ABANDONADO'
OTRO = 'OTRO'
ESTADO_TESIS_PROCESO_CHOICES = (
    (ACTIVO, capfirst(_('activo'))),
    (TERMINADO, capfirst(_('terminado'))),
    (ABANDONADO, capfirst(_('abandonado'))),
    (OTRO, capfirst(_('otro'))),
)

VENCIDO = 'VENCIDO'
CUMPLIDO = 'CUMPLIDO'
NO_CUMPLIDO = 'NO_CUMPLIDO'
ESTADO_TESIS_REQUISITO_CHOICES = (
    (VENCIDO, capfirst(_('vencido'))),
    (CUMPLIDO, capfirst(_('cumplido'))),
    (NO_CUMPLIDO, capfirst(_('no cumplido'))),
)
