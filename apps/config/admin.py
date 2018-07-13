from .models.menu import Menu
from .models.persona import Persona
from .models.perfil import Perfil
from django.contrib import admin

# Register your models here.
admin.site.register(Persona)
admin.site.register(Menu)
admin.site.register(Perfil)
