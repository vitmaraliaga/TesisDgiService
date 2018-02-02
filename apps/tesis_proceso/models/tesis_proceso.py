"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo TesisProceso.
"""
from apps.proceso.models.proceso import Proceso
from django.db import models
import datetime
from apps.tesis_proceso.models.base import Base
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from ..enums import ESTADO_TESIS_PROCESO_CHOICES, ACTIVO


class TesisProceso(Base):
    fecha_inicio = models.DateTimeField(capfirst(_('fecha de inicio')), default=datetime.datetime.now, blank=True)
    fecha_fin = models.DateTimeField(capfirst(_('fecha de fin')), null=True, blank=True)
    estado = models.CharField(capfirst(_('estado')), choices=ESTADO_TESIS_PROCESO_CHOICES, default=ACTIVO,
                              max_length=15)
    proceso = models.ForeignKey(Proceso, related_name='%(class)ss', verbose_name=capfirst(_('proceso')))

    class Meta:
        verbose_name = 'TesisProceso'
        verbose_name_plural = 'TesisProcesos'

    def __str__(self):
        return '%s Estado: %s' % (self.proceso.nombre, self.estado)
