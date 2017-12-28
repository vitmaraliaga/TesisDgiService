"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Etapa
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from .proceso import Proceso


# Create your models here.
class Etapa(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=100)
    descripcion = models.TextField(capfirst(_('descripción')), null=True, blank=True)
    proceso = models.ForeignKey(Proceso, related_name='%(class)s', verbose_name=capfirst(_('proceso')),
                                on_delete=models.CASCADE)
    # siguiente = models.ForeignKey('self', related_name='anteriores', verbose_name=capfirst(_('siguiente')),
    #                              null=True, blank=True)
    anterior = models.ForeignKey('self', related_name='siguientes', verbose_name=capfirst(_('anterior')),
                                 null=True, blank=True)
    plazo_dias = models.IntegerField(capfirst(_('plazo en dias')), null=True, blank=True, default=0)
    tarea_activador = models.ForeignKey('Tarea', related_name='%(class)s_activador',
                                        verbose_name=capfirst(_('tarea activador')), null=True, blank=True)
    tarea_desactivador = models.ForeignKey('Tarea', related_name='%(class)s_desactivador',
                                           verbose_name=capfirst(_('tarea desactivador')), null=True, blank=True)
    orden = models.IntegerField(capfirst(_('orden')), null=True, blank=True) #En realidad es not null. por problemas de migration se le pone asi.

    class Meta:
        verbose_name = 'etapa'
        verbose_name_plural = "etapas"

    def __str__(self):
        return '%s' % self.nombre
