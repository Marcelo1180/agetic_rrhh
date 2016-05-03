from django.contrib import admin
from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriado, TipoPermiso, DesignacionPermiso

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Horario)
admin.site.register(HorarioRango)
admin.site.register(DesignacionHorario)
admin.site.register(RegistroHorario)
admin.site.register(Feriado)
admin.site.register(TipoPermiso)
admin.site.register(DesignacionPermiso)
