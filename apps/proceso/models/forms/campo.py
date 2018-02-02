"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proceso.forms.campo

Description: modelo Campo
"""
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from ..base import Base
from .formulario import Formulario
from ...enums import TIPO_CAMPO_CHOICES, INPUT


class Campo(Base):
    """
    Model campo.
    """
    label = models.CharField(capfirst(_('label')), max_length=100)
    key = models.CharField(capfirst(_('key')), max_length=100, help_text="Este campo es único")  # this is unique.
    type = models.CharField(capfirst(_('type')), choices=TIPO_CAMPO_CHOICES, max_length=15, default=INPUT)
    required = models.BooleanField(capfirst(_('required')), default=False)
    flex = models.IntegerField(capfirst(_('flex')), null=True, blank=True, default=100,
                               help_text="width in %")  # width in %

    min = models.IntegerField(capfirst(_('min')), null=True, blank=True)
    max = models.IntegerField(capfirst(_('max')), null=True, blank=True)
    backgroud = models.CharField(capfirst(_('backgroud')), max_length=300, null=True, blank=True)
    model = models.CharField(capfirst(_('model')), max_length=200, null=True, blank=True,
                             help_text="Solo para selects")  # Solo para selects
    json = models.TextField(capfirst(_('json')), null=True, blank=True,
                            help_text="Solo para selects")  # Solo para selects
    formulario = models.ForeignKey(Formulario, related_name='%(class)ss', verbose_name=capfirst(_('formulario')),
                                   on_delete=models.CASCADE)
    icon = models.CharField(capfirst(_('icon')), max_length=50, null=True, blank=True)
    prefix = models.CharField(capfirst(_('prefix')), max_length=50, null=True, blank=True,
                              help_text="Útil para campos codigos telefonicos que van antes del numero. ej. 051, 054")
    hint_start = models.CharField(capfirst(_('hint_start')), max_length=200, null=True, blank=True,
                                  help_text="Texto de ayúda.")

    hint_end_count_text = models.BooleanField(capfirst(_('hint_end_count_text')), default=False,
                                              help_text="texto de ayúda Count del letras en el Input.")  # true or false
    disabled = models.BooleanField(capfirst(_('disabled')), default=False)
    multiselect = models.NullBooleanField(capfirst(_('multiselect')), default=False,
                                          help_text="Solo para selects")  # Only type select.
    order = models.IntegerField(capfirst(_('order')), null=True,
                                blank=True)  # En realidad es not null. por problemas de migration se le pone asi.

    class Meta:
        verbose_name = 'campo'
        verbose_name_plural = "campos"

    def __str__(self):
        return '%s (required: %s)' % (self.label, self.required)
