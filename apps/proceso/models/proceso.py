"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Proceso
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


# Create your models here.
class Proceso(Base):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'proceso'
        verbose_name_plural = "procesos"

    def __str__(self):
        return '%s' % self.nombre