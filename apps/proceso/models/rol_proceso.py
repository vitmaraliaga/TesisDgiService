"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Roles del proceso
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from .proceso import Proceso

# Create your models here.
class RolProceso(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=50)
    alias = models.CharField(capfirst(_('alias')), max_length=20, null=True, blank=True)
    descripcion = models.TextField(capfirst(_('descripción')), null=True, blank=True)
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    proceso = models.ForeignKey(Proceso, related_name='%(class)s', verbose_name=capfirst(_('proceso')),
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Rol de Proceso'
        verbose_name_plural = 'Roles de Proceso'

    def __str__(self):
        return '%s (%s)' % (self.alias, self.activo)
