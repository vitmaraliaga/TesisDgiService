"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.models

Description: modelo TesisRequisitoArchivo.
"""
from apps.tesis_proceso.models.tesis_requisito import TesisRequisito
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from .base import Base


class TesisRequisitoArchivo(Base):
    archivo = models.FileField(capfirst(_('archivo')), upload_to='tesis_requisito_archivo/archivos/',
                               default='tesis_requisito_archivo/archivos/none/default.pdf')
    imagen = models.ImageField(capfirst(_('foto')), upload_to='tesis_requisito_archivo/fotos/',
                               default='tesis_requisito_archivo/imagenes/none/default.png')
    tesis_requisito = models.ForeignKey(TesisRequisito, related_name='%(class)s',
                                        verbose_name=capfirst(_('tesis_requisito')),
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'TesisRequisitoArchivo'
        verbose_name_plural = 'TesisRequisitoArchivos'

    def __str__(self):
        return '%s (%s)' % self.tesis_requisito.requisito.id