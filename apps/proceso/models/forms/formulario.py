"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.form.formulario

Description: modelo Formulario
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from ..base import Base
from ..tarea import Tarea


class Formulario(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=300)
    alias = models.CharField(capfirst(_('alias')), max_length=100, null=True, blank=True)
    descripcion = models.TextField(capfirst(_('descripción')), null=True, blank=True)
    tarea = models.ForeignKey(Tarea, related_name='%(class)s', verbose_name=capfirst(_('tarea')),
                              on_delete=models.CASCADE)
    orden = models.IntegerField(capfirst(_('orden')), null=True,
                                blank=True)  # En realidad es not null. por problemas de migration se le pone asi.

    class Meta:
        verbose_name = 'formulario'
        verbose_name_plural = "formularios"

    def __str__(self):
        return '%s' % self.nombre
