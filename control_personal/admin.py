from django.contrib import admin
from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriados, TipoPermiso, DesignacionPermiso

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Horario)
admin.site.register(HorarioRango)
admin.site.register(DesignacionHorario)
admin.site.register(RegistroHorario)
admin.site.register(Feriados)
admin.site.register(TipoPermiso)
admin.site.register(DesignacionPermiso)
