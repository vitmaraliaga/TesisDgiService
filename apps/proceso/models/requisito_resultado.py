"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo RequisitoTarea
"""

from django.db import models
from .base import Base
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .requisito import Requisito
from .resultado import Resultado


# Create your models here.
class RequisitoResultado(Base):
    activo = models.BooleanField(capfirst(_('activo')), default=True)
    requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE, verbose_name=capfirst(_('requisito')))
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, verbose_name=capfirst(_('resultado')))

    class Meta:
        verbose_name = 'RequisitoResultado'
        verbose_name_plural = 'RequisitoResultados'
        ordering = ('requisito',)

    def __str__(self):
        return '%s-%s (%s)' % (self.requisito.nombre, self.resultado.nombre, self.activo)
