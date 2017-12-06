"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

Description: modelo Asesor.
"""
from apps.config.models.persona import Persona
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst

from .base import Base


class Asesor(Base):
    persona = models.OneToOneField(Persona, related_name='+', verbose_name=capfirst(_('persona')),
                                   on_delete=models.CASCADE)
    activo = models.BooleanField(capfirst(_('activo')), default=True)

    class Meta:
        verbose_name = 'Asesor'
        verbose_name_plural = 'Asesores'

    def __str__(self):
        return '%s %s' % (self.persona.nombres, self.persona.apellido_paterno)
