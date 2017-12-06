"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico.models

Description: modelo de DirectorInvestigacionEscuela.
"""
from .director_investigacion import DirectorInvestigacion
from .escuela import Escuela
from .base import Base
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class DirectorInvestigacionEscuela(Base):
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    fecha_inicio = models.DateField(capfirst(_('fecha de inicio')))
    fecha_fin = models.DateField(capfirst(_('fecha de finalización')), null=True, blank=True)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    director_investigacion = models.ForeignKey(DirectorInvestigacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'DirectorInvestigacionEscuela'
        verbose_name_plural = 'DirectorInvestigacionEscuelas'

    def __str__(self):
        return '%s %s (%s)' % (
            self.director_investigacion.persona.nombres, self.director_investigacion.persona.apellido_paterno,
            self.escuela.nombre)
