from django.contrib import admin
from apps.especialidades.models import Persona
from apps.especialidades.models import CentroEstudio
from apps.especialidades.models import Profesiones
from apps.especialidades.models import Capacitacion
from apps.especialidades.models import PerProfesion
from apps.especialidades.models import Experiencia
# Register your models here.
admin.site.register(Persona),
admin.site.register(CentroEstudio),
admin.site.register(Profesiones),
admin.site.register(Capacitacion),
admin.site.register(PerProfesion),
admin.site.register(Experiencia) ,






