from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


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

    def clean(self):
        if self.hora_entrada <= self.rango_entrada_ini:
            raise ValidationError('Error la hora de entrada debe ser mayor al rango de entrada de inicio')

        if self.hora_entrada > self.hora_salida:
            raise ValidationError('Error la hora de entrada debe ser menor o igual a la hora de salida')

        if self.hora_salida >= self.rango_salida_fin:
            raise ValidationError('Error la hora de salida debe ser menor al rango de salida final')

        if self.rango_entrada_ini > self.rango_entrada_fin:
            raise ValidationError('Error el rango de entrada de inicio debe ser menor o igual al rango de entrada final')

        if self.rango_entrada_fin >= self.rango_salida_ini:
            raise ValidationError('Error el rango de entrada debe ser menor al rango de salida')

        if self.rango_salida_ini > self.rango_salida_fin:
            raise ValidationError('Error el rango de salida de inicio debe ser menor o igual al rango de salida final')

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

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


BOOL_APROBADO = (
    (True, 'Aprobado'),
    (False, 'No Aprobado')
)


class DesignacionPermiso(models.Model):
    tipo_permiso = models.ForeignKey(TipoPermiso)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User)
    fecha_ini = models.DateField()
    fecha_fin = models.DateField()
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    jefe = models.ForeignKey(User, related_name='jefe')
    token_mail = models.CharField(max_length=250)
    token_confirmation_date = models.DateTimeField(blank=True, null=True)
    aprobado = models.BooleanField(choices=BOOL_APROBADO, default=False)

    def clean(self):
        if self.fecha_ini > self.fecha_fin:
            raise ValidationError('Error la fecha de inicio debe ser menor o igual a la fecha final')

        if self.hora_ini and not self.hora_fin:
            raise ValidationError('Si registra una hora de inicio debe colocar una hora final')

        if self.hora_ini and self.hora_fin:
            if self.hora_ini > self.hora_fin:
                raise ValidationError('Error la hora de inicio debe ser menor o igual a la hora final')

    def save(self, *args, **kwargs):
        # COLOCAR AQUI CONSUMIR EL REST DE ORGANIGRAMA
        # Envio un uid y me devuelve el uid del jefe, si este esta inactivo me devuelve la del superior
        self.jefe = User.objects.get(pk=1)

        # Crear un Token Para confirmacion de Permiso mediante correo, por temas de la url cambio el separador por -
        from django.core.signing import TimestampSigner
        signer = TimestampSigner(salt="4g3t1c")
        self.token_mail = signer.sign(self.pk)

        super(DesignacionPermiso, self).save(*args, **kwargs)

    def __str__(self):
        return "%s: %s - %s" % (self.tipo_permiso, self.fecha_ini, self.fecha_fin)

    def __unicode__(self):
        return "%s: %s - %s" % (self.tipo_permiso, self.fecha_ini, self.fecha_fin)


# TENGO QUE CREAR OTRA APP DONDE ESTEN LOS MODULOS DEL OTRO SISTEMA
# QUE RIGISTRE LAS IP DE LOS BIOMETRICOS Y LOS CONSUMA EN UNA BASE DE DATOS
