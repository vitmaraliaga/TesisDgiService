"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico.models

Description: modelo de LineaInvestigacion.
"""
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from .base import Base
from .escuela import Escuela


class LineaInvestigacion(Base):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    escuela = models.ForeignKey(Escuela, verbose_name=capfirst(_('escuela')), related_name='%(class)ss',
                                null=True, blank=True)

    class Meta:
        verbose_name = 'LineaInvestigacion'
        verbose_name_plural = 'LineaInvestigacions'

    def __str__(self):
        return '%s' % self.nombre