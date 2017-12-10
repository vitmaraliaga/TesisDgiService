"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

Description: modelo Proyecto.
"""
from apps.academico.models.linea_investigacion import LineaInvestigacion
from apps.tesis_proceso.models.tesis_proceso import TesisProceso
from .tesista import Tesista
from .jurado import Jurado
from .asesor import Asesor
from .dictaminador import Dictaminador
from .base import Base
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from ..enums import ESTADO_PROYECTO_CHOICES, PROCESO


class Proyecto(Base):
    titulo = models.CharField(capfirst(_('título')), max_length=500)
    resumen = models.TextField(capfirst(_('resumen')), null=True, blank=True)
    archivo = models.FileField(capfirst(_('archivo')), upload_to='proyecto/archivos/',
                               default='proyecto/archivos/none/default.pdf')
    fecha_fin = models.DateTimeField(capfirst(_('fecha de finalización')), null=True, blank=True)
    estado = models.CharField(capfirst(_('estado')), choices=ESTADO_PROYECTO_CHOICES, max_length=15, default=PROCESO)
    fecha_sustentacion = models.DateTimeField(capfirst(_('fecha de sustentación')), null=True, blank=True)

    dictaminador = models.ManyToManyField(Dictaminador, through='ProyectoDictaminador',
                                          through_fields=('proyecto', 'dictaminador'))
    asesor = models.ManyToManyField(Asesor, through='ProyectoAsesor', through_fields=('proyecto', 'asesor'))
    jurado = models.ManyToManyField(Jurado, through='ProyectoJurado', through_fields=('proyecto', 'jurado'))
    tesista = models.ManyToManyField(Tesista)
    linea_investigacion = models.ManyToManyField(LineaInvestigacion)
    tesis_proceso = models.OneToOneField(TesisProceso, related_name='%(class)s', verbose_name=capfirst(_('proceso')),
                                   null=True, blank=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return '%s ( %s )' % (
            self.titulo, ', '.join(['%s %s' % (a.persona.nombres, a.persona.apellido_paterno) for a in self.tesista.all()]))
