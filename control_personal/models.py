from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Funcionario(models.Model):
    # user = models.OneToOneField(User)
    uid = models.CharField(max_length=50)
    estado = models.BooleanField(default=False, help_text='El usuario esta activo en el sistema')


# ASIGNACION DE HORARIO QUE EL FUNCIONARIO DEBE CUMPLIR
class Horario(models.Model):
    descripcion = models.CharField(max_length=100)
    observacion = models.TextField()
    # estado = models.BooleanField(default=False, help_text='Un libro es considerado de Referencia si')
    sw_tolerancia_acumulada = models.BooleanField(default=True, help_text='Trabajar con el modo de tolerancia acumulada')
    tolerancia_acumulada = models.IntegerField()

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class HorarioRango(models.Model):
    horario = models.ForeignKey(Horario)
    descripcion = models.CharField(max_length=100)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    rango_entrada_ini = models.TimeField()
    rango_entrada_fin = models.TimeField()
    rango_salida_ini = models.TimeField()
    rango_salida_fin = models.TimeField()
    tolerancia_individual = models.IntegerField(default=0, help_text='Si el modo de tolerancia acumulada se encuentra desactivada puede utilizar este tipo de tolerancia, caso contrario dejar en 0')

    def __str__(self):
        return "%s: %s - %s" % (self.horario, self.hora_entrada, self.hora_salida)

    def __unicode__(self):
        return "%s: %s - %s" % (self.horario, self.hora_entrada, self.hora_salida)


class DesignacionHorario(models.Model):
    usuario = models.ForeignKey(User)
    horario = models.ForeignKey(Horario)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    def clean(self):
        from django.core.exceptions import ValidationError
        # Don't allow draft entries to have a pub_date.
        if self.fecha_ini > self.fecha_fin:
            raise ValidationError('Error la fecha de inicio debe ser menor o igual a la fecha final')
# PROBAR SI FUNCIONA EN EL POSTMAN Y SI ME VOTA EL ERROR CON REST JSON


# REGISTRO DE ASISTENCIA DE USUARIO AL DIA
class RegistroHorario(models.Model):
    hora = models.TimeField()
    fecha = models.DateField()
    uid = models.CharField(max_length=50)
    biometrico = models.CharField(max_length=100)


# TABLA DE FERIADOS REGISTRADOS EN EL SISTEMA
class Feriado(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha = models.DateField()


# REGISTRO DE PERMISOS
class TipoPermiso(models.Model):
    descripcion = models.CharField(max_length=200)


class DesignacionPermiso(models.Model):
    tipo_permiso = models.ForeignKey(TipoPermiso)
    descripcion = models.CharField(max_length=200)
    funcionario = models.ForeignKey(Funcionario)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    hora_ini = models.TimeField()
    hora_fin = models.TimeField()


# TENGO QUE CREAR OTRA APP DONDE ESTEN LOS MODULOS DEL OTRO SISTEMA
# QUE RIGISTRE LAS IP DE LOS BIOMETRICOS Y LOS CONSUMA EN UNA BASE DE DATOS
