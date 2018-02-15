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
from .campo import Campo
from .validation import Validation


class CampoValidation(Base):
    data = models.CharField(capfirst(_('data')), max_length=200, null=True, blank=True)
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE, verbose_name=capfirst(_('campo')))
    validation = models.ForeignKey(Validation, on_delete=models.CASCADE, verbose_name=capfirst(_('validation')))

    class Meta:
        verbose_name = 'CampoValidation'
        verbose_name_plural = "CampoValidations"
        ordering = ('campo',)

    def __str__(self):
        return '%s %s' % (self.campo.name, self.validation.nombre )
