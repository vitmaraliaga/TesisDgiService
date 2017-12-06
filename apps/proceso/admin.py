from django.contrib import admin
from .models.proceso import Proceso
from .models.etapa import Etapa
from .models.requisito import Requisito
from .models.requisito_resultado import RequisitoResultado
from .models.resultado import Resultado
from .models.rol_proceso import RolProceso
from .models.tarea import Tarea

# Register your models here.
admin.site.register(Proceso)
admin.site.register(Etapa)
admin.site.register(Requisito)
admin.site.register(RequisitoResultado)
admin.site.register(Resultado)
admin.site.register(RolProceso)
admin.site.register(Tarea)

