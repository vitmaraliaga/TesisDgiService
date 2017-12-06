"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso

Description: Enums de la aplicación
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


NORMAL = 'NORMAL'
TEMPORIZADOR = 'TEMPORIZADOR'
TIPO_REQUISITO_CHOICES = (
    (NORMAL, capfirst(_('requisito normal'))),
    (TEMPORIZADOR, capfirst(_('requisito temporizador'))),
)

