"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package auth.models

Description: modelo Menu.
"""
from apps.config.enums import NIVEL_CHOICES, PRIMERO
from django.db import models

from apps.config.models.base import Base
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class Menu(Base):
    titulo = models.CharField(capfirst(_('título')), max_length=50)
    descripcion = models.CharField(capfirst(_('descripcion')), max_length=50, null=True, blank=True)
    url = models.CharField(capfirst(_('url')), max_length=50, default="#", null=True, blank=True)
    icono = models.CharField(capfirst(_('icono')), max_length=15, null=True, blank=True)
    activo = models.DateField(capfirst(_('activo')), default=True)
    parent = models.ForeignKey('self', related_name='hijos', verbose_name=capfirst(_('parent')), null=True, blank=True )
    nivel = models.CharField(capfirst(_('nivel')), choices=NIVEL_CHOICES, default=PRIMERO, max_length=1)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return '%s (%s) %s' % (self.titulo, self.url, dict((x, y) for x, y in NIVEL_CHOICES)[self.nivel])
