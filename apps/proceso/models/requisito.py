"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Requisito
"""

from django.db import models
from .base import Base
from ..enums import TIPO_REQUISITO_CHOICES, NORMAL
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Requisito(Base):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    plazo_dias = models.IntegerField(capfirst(_('plazo en dias')), null=True, blank=True, default=0)
    tipo = models.CharField(capfirst(_('tipo')), choices=TIPO_REQUISITO_CHOICES, max_length=15, default=NORMAL)

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        ordering = ('nombre',)

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.activo)
