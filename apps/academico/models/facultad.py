"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico.models

Description: modelo de Facultad.
"""
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from .base import Base


class Facultad(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=200)
    alias = models.CharField(capfirst(_('alias')), max_length=200, null=True, blank=True)
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    logo = models.ImageField(capfirst(_('logo')), upload_to='escuela/logos/', default='escuela/logos/none/default.png')
    tema = models.CharField(capfirst(_('tema')), default='default-theme', max_length=20)
    mision = models.TextField(capfirst(_('misión')), max_length=1000, null=True, blank=True)
    vision = models.TextField(capfirst(_('visión')), max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'

    def __str__(self):
        return '%s' % self.nombre
