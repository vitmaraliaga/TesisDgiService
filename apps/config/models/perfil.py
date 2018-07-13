"""
@copyright Copyright (c) 2017  DevOtion Team
@author Vitmar Aliaga (@cruzjhonson)
@package auth.models

Description: modelo Perfil. Éste modelo se encargará de 
unir a todas las personas de académico. y darles un Usuario en el sistema
"""
from django.db import models

from .base import Base
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .persona import Persona

class Perfil(Base):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(usuario=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return '%s' % (self.usuario.username)
