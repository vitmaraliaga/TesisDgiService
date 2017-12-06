"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

Description: modelo ProyectoJurado => Tabla relacion ManyToMany entre Proyecto y Jurado.
"""
from .jurado import Jurado
from .proyecto import Proyecto
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from ..enums import TIPO_JURADO_CHOICES, PRESIDENTE


class ProyectoJurado(Base):
    tipo = models.CharField(capfirst(_('etapa')), choices=TIPO_JURADO_CHOICES, max_length=15, default=PRESIDENTE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    jurado = models.ForeignKey(Jurado, on_delete=models.CASCADE)
    activo = models.BooleanField(capfirst(_('activo')), default=True)

    class Meta:
        verbose_name = 'ProyectoJurado'
        verbose_name_plural = 'ProyectoJurados'

    def __str__(self):
        return '%s (%s %s) (%s)' % (
            self.proyecto.titulo, self.jurado.persona.nombres, self.jurado.persona.apellido_paterno, self.tipo)
