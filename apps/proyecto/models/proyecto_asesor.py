"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

Description: modelo ProyectoAsesor => Tabla relacion ManyToMany entre Proyecto y Asesor.
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from .base import Base
from ..enums import TIPO_ASESOR_CHOICES, ASESOR
from .proyecto import Proyecto
from .asesor import Asesor


class ProyectoAsesor(Base):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    asesor = models.ForeignKey(Asesor, on_delete=models.CASCADE)
    tipo = models.CharField(capfirst(_('tipo')), choices=TIPO_ASESOR_CHOICES, max_length=15, default=ASESOR)
    activo = models.BooleanField(capfirst(_('activo')), default=True)

    class Meta:
        verbose_name = 'ProyectoAsesor'
        verbose_name_plural = 'ProyectoAsesores'

    def __str__(self):
        return 'PROYECTO: %s : ASESOR: (%s %s)' % (self.proyecto.titulo, self.asesor.persona.nombres, self.asesor.persona.apellido_paterno)
