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
from .validation import Validation
from ...enums import TIPO_CAMPO_CHOICES, INPUT, TIPO_VALIDADOR_CHOICES, GRUPAL


class Campo(Base):
    """
    Model campo.
    """
    label = models.CharField(capfirst(_('label')), max_length=100)
    # key = models.CharField(capfirst(_('key')), max_length=100, help_text="Este campo es único")  # this is unique.
    name = models.CharField(capfirst(_('name')), max_length=100, help_text="Este campo es único 'is key' ")  # this is unique.
    type = models.CharField(capfirst(_('type')), choices=TIPO_CAMPO_CHOICES, max_length=15, default=INPUT)
    required = models.BooleanField(capfirst(_('required')), default=False)
    # flex = models.IntegerField(capfirst(_('flex')), null=True, blank=True, default=100,
                            #    help_text="width in %")  # width in %
    width = models.IntegerField(capfirst(_('width')), null=True, blank=True, default=100,
                               help_text="width in %")  # width in %
    validation = models.ManyToManyField(Validation, through='CampoValidation',
                                        through_fields=('campo', 'validation'))
    # min = models.IntegerField(capfirst(_('min')), null=True, blank=True)
    # max = models.IntegerField(capfirst(_('max')), null=True, blank=True)
    # backgroud = models.CharField(capfirst(_('backgroud')), max_length=300, null=True, blank=True)
    placeholder = models.CharField(capfirst(_('placeholder')), max_length=300, null=True, blank=True)
    model_name = models.CharField(capfirst(_('model_name')), max_length=200, null=True, blank=True,
                             help_text="Solo para selects")  # Solo para selects
    model_pk = models.CharField(capfirst(_('model_pk')), max_length=200, null=True, blank=True,
                             help_text="Solo para selects")  # Solo para selects
    model_label = models.CharField(capfirst(_('model_label')), max_length=200, null=True, blank=True,
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

    accept_fileinput = models.CharField(capfirst(_('Aceept for Fileinput')), 
                            null= True, blank = True, max_length = 500,
                            help_text="Extención de los archivos que se puede adjuntar") # Solo para FileInputs
    multiple_fileinput = models.BooleanField(capfirst(_('multiple')),
                            default = False,
                            help_text="Si el File input es para multiples Erchivos") # Solo para Fileinputs

    # Solo cuqndo el campo es de tipo validador
    tipo_validador = models.CharField(capfirst(_('tipo_validador')), choices=TIPO_VALIDADOR_CHOICES, max_length=15, null= True, blank = True)
    # En este campo se guardará los Ids(en un cadena separada por comas) de los roles que pueden validar el campo
    roles_validadores =  models.CharField(capfirst(_('roles_validadores')), max_length=500, null= True, blank = True)

    class Meta:
        verbose_name = 'campo'
        verbose_name_plural = "campos"

    def __str__(self):
        return '%s (required: %s)' % (self.label, self.required)
