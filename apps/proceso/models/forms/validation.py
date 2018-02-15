"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.forms.validation

Description: modelo Validation
"""
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from ..base import Base
# from .formulario import Formulario
# from ...enums import TIPO_CAMPO_CHOICES, INPUT


class Validation(Base):
    nombre = models.CharField(capfirst(_('nombre')), max_length=50)
    key = models.CharField(capfirst(_('key')), max_length=50)
    
    class Meta:
        verbose_name = 'validation'
        verbose_name_plural = "validations"

    def __str__(self):
        return '%s' % self.nombre
