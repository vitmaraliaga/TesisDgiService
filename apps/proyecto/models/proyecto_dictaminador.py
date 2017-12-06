"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

Description: modelo ProyectoDictaminador => Tabla relacion ManyToMany entre Proyecto y Dictaminador.
"""
from .dictaminador import Dictaminador
from .proyecto import Proyecto
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from ..enums import ETAPAS_CHOICES, PROYECTO


class ProyectoDictaminador(Base):
    tipo = models.CharField(capfirst(_('etapa')), choices=ETAPAS_CHOICES, max_length=15, default=PROYECTO)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    dictaminador = models.ForeignKey(Dictaminador, on_delete=models.CASCADE)
    activo = models.BooleanField(capfirst(_('activo')), default=True)

    class Meta:
        verbose_name = 'ProyectoDictaminador'
        verbose_name_plural = 'ProyectoDictaminadors'

    def __str__(self):
        return '%s (%s %s) (%s)' % (
            self.proyecto.titulo, self.dictaminador.persona.nombres, self.dictaminador.persona.apellido_paterno, self.tipo)
