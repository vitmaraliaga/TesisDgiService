"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.forms.campo_valor

Description: modelo Etapa
"""

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _

from ..base import Base
from .campo import Campo
from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from apps.tesis_proceso.models.tesis_etapa import TesisEtapa
from apps.tesis_proceso.models.tesis_tarea import TesisTarea


class CampoValor(Base):
    valorInput = models.CharField(capfirst(_('valorInput')), max_length=300, blank=True, null=True),
    valorTextArea = models.CharField(capfirst(_('textArea')), blank=True, null=True),

    valorFileInput = models.FileField(capfirst(_('valorFileInput')), upload_to='proceso/valor-file-inputs/',
                                      #    default='proceso/valor-file-inputs/none/default.pdf',
                                      blank=True, null=True)

    campo = models.ForeignKey(Campo, related_name='%(class)s', verbose_name=capfirst(_('campo')),
                              on_delete=models.CASCADE)
    tesis_proceso = models.ForeignKey(TesisProceso, related_name='%(class)s', verbose_name=capfirst(_('TesisProceso')),
                                      on_delete=models.CASCADE),
    tesis_etapa = models.ForeignKey(TesisEtapa, related_name='%(class)s', verbose_name=capfirst(_('TesisEtapa')),
                                    on_delete=models.CASCADE),
    tesis_tarea = models.ForeignKey(TesisTarea, related_name='%(class)s', verbose_name=capfirst(_('TesisTarea')),
                                    on_delete=models.CASCADE),

    class Meta:
        verbose_name = 'campoValor'
        verbose_name_plural = "campoValors"

    def __str__(self):
        return '%s' % self.nombre
