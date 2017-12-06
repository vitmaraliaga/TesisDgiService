"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Requisito
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


# Create your models here.
class Resultado(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=50)
    descripcion = models.TextField(capfirst(_('descripción')), blank=True, null=True)

    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'

    def __str__(self):
        return '%s' % self.nombre
