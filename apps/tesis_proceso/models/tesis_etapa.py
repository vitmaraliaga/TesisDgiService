"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo TesisEtapa.
"""
from apps.proceso.models.etapa import Etapa
from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


class TesisEtapa(Base):
    etapa = models.ForeignKey(Etapa, related_name='%(class)s', verbose_name=capfirst(_('etapa')))
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    fecha_inicio = models.DateTimeField(capfirst(_('fecha de inicio')), null=True, blank=True)
    fecha_fin = models.DateTimeField(capfirst(_('fecha fin')), null=True, blank=True)
    tesis_proceso = models.ForeignKey(TesisProceso, related_name='%(class)s', verbose_name=capfirst(_('tesis_proceso')),
                                      blank=True, null=True)

    class Meta:
        verbose_name = 'TesisEtapa'
        verbose_name_plural = 'TesisEtapas'

    def __str__(self):
        return '%s (%s)' % (self.etapa.nombre, self.activo)
