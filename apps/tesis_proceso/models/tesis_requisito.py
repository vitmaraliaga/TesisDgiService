"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo TesisRequisito.
"""
from apps.proceso.models.requisito import Requisito
from apps.proceso.models.resultado import Resultado
from apps.tesis_proceso.models.tesis_tarea import TesisTarea
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from ..enums import ESTADO_TESIS_REQUISITO_CHOICES, NO_CUMPLIDO


class TesisRequisito(Base):
    estado = models.CharField(capfirst(_('estado')), choices=ESTADO_TESIS_REQUISITO_CHOICES, default=NO_CUMPLIDO,
                              max_length=15)
    informacion_adicional = models.TextField(null=True, blank=True)
    requisito = models.ForeignKey(Requisito, related_name='%(class)ss',
                                  verbose_name=capfirst(_('requisito')))
    resultado = models.ForeignKey(Resultado, related_name='%(class)ss',
                                  verbose_name=capfirst(_('resultado')))
    tesis_tarea = models.ForeignKey(TesisTarea, related_name='%(class)ss', verbose_name=capfirst(_('tesis_tarea')),
                                    blank=True, null=True)

    class Meta:
        verbose_name = 'TesisRequisito'
        verbose_name_plural = 'TesisRequisitos'

    def __str__(self):
        return '%s (%s)' % (self.requisito.nombre, self.estado)
