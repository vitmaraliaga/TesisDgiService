"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package proyecto.models

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

    class Meta:
        abstract = True
