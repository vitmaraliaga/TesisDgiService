"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package auth.models

Description: modelo Base.
"""
from uuid import uuid4

from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fecha_creacion = models.DateTimeField(capfirst(_('fecha de creación')), auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(capfirst(_('fecha de actualización')), auto_now=True, null=True)

    # usuario_creacion = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=capfirst(_('usuario de creación')),
    #                                     related_name='tareas_created', editable=False)
    # usuario_actualizacion = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                                          verbose_name=capfirst(_('usuario de actualización')),
    #                                          blank=True, null=True)

    class Meta:
        abstract = True
