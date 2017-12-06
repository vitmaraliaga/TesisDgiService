from .models.director_investigacion_escuela import DirectorInvestigacionEscuela
from .models.director_investigacion import DirectorInvestigacion
from .models.escuela import Escuela
from .models.facultad import Facultad
from .models.linea_investigacion import LineaInvestigacion
from django.contrib import admin

# Register your models here.
admin.site.register(Facultad)
admin.site.register(Escuela)
admin.site.register(LineaInvestigacion)
admin.site.register(DirectorInvestigacion)
admin.site.register(DirectorInvestigacionEscuela)
