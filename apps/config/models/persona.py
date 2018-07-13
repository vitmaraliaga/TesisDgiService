"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package auth.models

Description: modelo Persona.
"""
from django.db import models

from .base import Base
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from ..enums import GENERO_CHOICES, MASCULINO

class Persona(Base):
    nombres = models.CharField(capfirst(_('nombres')), max_length=50)
    apellido_paterno = models.CharField(capfirst(_('apellido paterno')), max_length=50)
    apellido_materno = models.CharField(capfirst(_('apellido materno')), max_length=50)
    genero = models.CharField(capfirst(_('género')), max_length=1, choices=GENERO_CHOICES, default=MASCULINO)
    fecha_nacimiento = models.DateField(capfirst(_('fecha de nacimiento')))
    direccion = models.CharField(capfirst(_('dirección')), null=True, blank=True, max_length=500)
    telefono = models.CharField(capfirst(_('teléfono')), null=True, blank=True, max_length=12)
    celular = models.CharField(capfirst(_('celular')), null=True, blank=True, max_length=12)
    num_doc = models.CharField(capfirst(_('dni')), help_text=capfirst(_('número de documento nacional de identidad')),
                               null=True, blank=True, unique=True, max_length=8)
    carnet_extrangeria = models.CharField(capfirst(_('carnet de extrangería')),
                                          help_text=capfirst(_('número de carnet de extrangería')), null=True,
                                          blank=True, max_length=12)
    foto = models.ImageField(capfirst(_('foto')), upload_to='personas/fotos/', default='personas/fotos/none/default.png')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return '%s %s %s (%s)' % (self.nombres, self.apellido_paterno, self.apellido_materno, self.num_doc)
