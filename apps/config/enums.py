"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package auth

Description: Enums de la aplicación
"""
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


MASCULINO = 'M'
FEMENINO = 'F'
GENERO_CHOICES = (
    (MASCULINO, capfirst(_('masculino'))),
    (FEMENINO, capfirst(_('femenino'))),
)

PRIMERO = '1'
SEGUNDO = '2'
TERCERO = '3'
NIVEL_CHOICES = (
    (PRIMERO, capfirst(_('primer nivel'))),
    (SEGUNDO, capfirst(_('segundo nivel'))),
    (TERCERO, capfirst(_('tercer nivel'))),
)

