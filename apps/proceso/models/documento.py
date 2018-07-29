"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Documento
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base

# Create your models here.
class Documento(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=100)
    alias = models.CharField(capfirst(_('alias')), max_length=50)
    descripcion = models.TextField(capfirst(_('descripción')), null=True, blank=True)
    llave_documento = models.CharField(capfirst(_('llave documento')), max_length=60)
    activo = models.BooleanField(capfirst(_('activo')), default=True)

    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = "documentos"

    def __str__(self):
        return '%s' % self.nombre
