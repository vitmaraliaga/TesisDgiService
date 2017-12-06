from .models.observacion import Observacion
from .models.tesis_etapa import TesisEtapa
from .models.tesis_proceso import TesisProceso
from .models.tesis_requisito import TesisRequisito
from .models.tesis_requisito_archivo import TesisRequisitoArchivo
from .models.tesis_tarea import TesisTarea
from django.contrib import admin

# Register your models here.
admin.site.register(Observacion)
admin.site.register(TesisEtapa)
admin.site.register(TesisProceso)
admin.site.register(TesisRequisito)
admin.site.register(TesisRequisitoArchivo)
admin.site.register(TesisTarea)
