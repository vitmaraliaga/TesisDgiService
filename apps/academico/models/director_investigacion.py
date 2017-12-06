"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico.models

Description: modelo de DirectorInvestigacion.
"""
from .escuela import Escuela
from apps.config.models.persona import Persona
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


class DirectorInvestigacion(Base):
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    persona = models.OneToOneField(Persona, related_name='+', verbose_name=capfirst(_('persona')),
                                   on_delete=models.CASCADE)
    escuela = models.ManyToManyField(Escuela, through='DirectorInvestigacionEscuela',
                                     through_fields=('director_investigacion', 'escuela'))

    class Meta:
        verbose_name = 'DirectorInvestigacion'
        verbose_name_plural = 'DirectorInvestigaciones'

    def __str__(self):
        return '%s %s' % (self.persona.nombres, self.persona.apellido_paterno)
