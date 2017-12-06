"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Observacion.
"""
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


# from django.conf import Settings


class Observacion(Base):
    titulo = models.CharField(capfirst(_('título')), max_length=150)
    descripcion = models.TextField(capfirst(_('descripción')), max_length=500)
    # emisor = models.ForeignKey(Settings.USE)
    fecha_envio = models.DateTimeField(capfirst(_('fecha de envio')), null=True, blank=True)
    fecha_leido = models.DateTimeField(capfirst(_('fecha de lectura')), null=True, blank=True)

    class Meta:
        verbose_name = 'Observacion'
        verbose_name_plural = 'Observaciones'

    def __str__(self):
        return '%s ' % self.titulo
