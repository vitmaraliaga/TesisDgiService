"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo Tarea
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from .etapa import Etapa
from .requisito_resultado import RequisitoResultado
from .rol_proceso import RolProceso


# Create your models here.
class Tarea(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=100)
    descripcion = models.TextField(capfirst(_('descripcion')), null=True, blank=True)
    etapa = models.ForeignKey(Etapa, related_name='%(class)s', verbose_name=capfirst(_('etapa')),
                              on_delete=models.CASCADE)
    anterior = models.ForeignKey('self', related_name='siguiente', verbose_name=capfirst(_('anterior')),
                                  null=True, blank=True)
    rol_ejecuta = models.ManyToManyField(RolProceso)
    plazo_dias = models.IntegerField(capfirst(_('plazo en dias')), null=True, blank=True, default=0)
    req_res_activador = models.ForeignKey(RequisitoResultado, related_name='+',
                                          verbose_name=capfirst(_('requisito resultado activador')), null=True,
                                          blank=True)
    req_res_desactivador = models.ForeignKey(RequisitoResultado, related_name='+',
                                             verbose_name=capfirst(_('requisito resultado desactivador')), null=True,
                                             blank=True)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return '%s (%s)' % (self.nombre, ', '.join([a.nombre for a in self.rol_ejecuta.all()]))
