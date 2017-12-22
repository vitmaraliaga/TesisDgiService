"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package academico.models

Description: modelo de Escuela.
"""
import uuid
from .facultad import Facultad
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base
from django.db import models

def scramble_logo_filename(instance, filename):
    extension = filename.split(".")[-1]
    # return "{}.{}".format("filename", extension) 
    return "escuela/logos/{}.{}".format(uuid.uuid4(), extension) 

class Escuela(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=200)
    alias = models.CharField(capfirst(_('alias')), max_length=200, null=True, blank=True)
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    # logo = models.ImageField(capfirst(_('logo')), upload_to=scramble_logo_filename, default='escuela/logos/none/default.png')
    logo = models.ImageField(capfirst(_('logo')), upload_to='escuela/logos/', 
                                            default='escuela/logos/none/default.png', null=True, blank=True)
    mision = models.TextField(capfirst(_('misión')), max_length=1000, null=True, blank=True)
    vision = models.TextField(capfirst(_('vision')), max_length=1000, null=True, blank=True)
    facultad = models.ForeignKey(Facultad, verbose_name=capfirst(_('facultad')), related_name='%(class)s')

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'

    def __str__(self):
        return '%s ' % self.nombre
