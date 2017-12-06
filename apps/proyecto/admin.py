from .models.asesor import Asesor
from .models.dictaminador import Dictaminador
from .models.jurado import Jurado
from .models.proyecto import Proyecto
from .models.proyecto_asesor import ProyectoAsesor
from .models.proyecto_dictaminador import ProyectoDictaminador
from .models.proyecto_jurado import ProyectoJurado
from .models.tesista import Tesista
from django.contrib import admin

# Register your models here.
admin.site.register(Asesor)
admin.site.register(Dictaminador)
admin.site.register(Jurado)
admin.site.register(Proyecto)
admin.site.register(ProyectoAsesor)
admin.site.register(ProyectoDictaminador)
admin.site.register(ProyectoJurado)
admin.site.register(Tesista)
