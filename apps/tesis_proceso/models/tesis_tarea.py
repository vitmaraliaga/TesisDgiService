"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo TesisTarea.
"""
from apps.proceso.models.tarea import Tarea
from apps.tesis_proceso.models.tesis_etapa import TesisEtapa
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


class TesisTarea(Base):
    tarea = models.ForeignKey(Tarea, related_name='%(class)ss', verbose_name=capfirst(_('tarea')))
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    fecha_inicio = models.DateTimeField(capfirst(_('fecha de inicio')))
    fecha_fin = models.DateTimeField(capfirst(_('fecha de finalizaciòn')))
    tesis_etapa = models.ForeignKey(TesisEtapa, related_name='%(class)ss', verbose_name=capfirst(_('tesis_etapa')),
                                    blank=True, null=True)

    class Meta:
        verbose_name = 'TesisTarea'
        verbose_name_plural = 'TesisTareas'

    def __str__(self):
        return '%s (%s)' % self.tarea.nombre, self.activo
