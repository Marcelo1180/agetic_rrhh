#!/usr/bin/python
# -*- coding: utf8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from models import DesignacionPermiso
from django.utils import timezone


def home(request):
    # return render(request, 'biblioteca/home.html')
    # return render(request, 'biblioteca/reporte/ingreso_libros.html')
    HttpResponse("Hola mundo")


from django.core import signing
from django.core.signing import TimestampSigner


def confirmar_permiso(request):
    """
    ## Confirma un permiso enviado por la url

    Estado=Aprobado
    http://127.0.0.1:8000/confirmar/permiso/?token=4:1ay4mm:xeXW4JDTQqU3JYtVC-l_He1gT08&estado=1

    Estado=No Aprobado
    http://127.0.0.1:8000/confirmar/permiso/?token=4:1ay4mm:xeXW4JDTQqU3JYtVC-l_He1gT08&estado=0

    La utilidad de esta liibreria es para otorgar un permiso via email
    """
    token_mail = request.GET.get("token")
    estado = True if request.GET.get("estado") == "1" else False
    print estado
    print token_mail
    signer = TimestampSigner(salt="4g3t1c")
    try:
        pk_dpermiso = signer.unsign(token_mail, max_age=3600*1)
        designacion_permiso = DesignacionPermiso.objects.filter(pk=pk_dpermiso, token_mail=token_mail, token_confirmation_date__isnull=True)
        if designacion_permiso:
            designacion_permiso.update(aprobado=estado, token_confirmation_date=timezone.now())
            return HttpResponse("El permiso fue aprobado satisfactoriamente")
        else:
            return HttpResponse("El permiso ya fue confirmado")
    except signing.SignatureExpired:
        return HttpResponse("La clave del mensaje a expirado")
    except signing.BadSignature:
        return HttpResponse("Firma de Mensaje Incorrecto")
# ----------------------------------------------------------------------------------------------
# REST
# ----------------------------------------------------------------------------------------------
from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriado, TipoPermiso, DesignacionPermiso
from serializers import HorarioSerializer, HorarioRangoSerializer, DesignacionHorarioSerializer, RegistroHorarioSerializer, FeriadoSerializer, TipoPermisoSerializer, DesignacionPermisoSerializer
from rest_framework import viewsets
from permissions import HorarioPermission


# REST TABLES
class HorarioViewSet(viewsets.ModelViewSet):
    """
    ## Establecer un Horario en el sistema
    Se define un tipo horario que contendra un rango de horarios para que los funcionarios puedan marcar

    __sw_tolerancia_acumulada__ Se activa el modo de tolerancia acumulada

    __tolerancia_acumulada__ La tolerancia acumulada es el tiempo en minutos que tiene un funcionario de tolerancia en un dia
    """
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    # permission_classes = (HorarioPermission,)

# algoritmo para llenar la tabla de marcados, hacer una tabla de marcados
class HorarioRangoViewSet(viewsets.ModelViewSet):
    """
    ## Establecer un Rango de Horas para un Horario
    Se define un rango de horarios para identificar cual de los marcados corresponden a la entrada o salida definida en un rango de horarios

    __tolerancia_individual__ La tolerancia individual es el tiempo en minutos que tiene un funcionario de tolerancia en un rango,
    se tomara esta tolerancia si es que la __sw_tolerancia_acumulada__ no esta activa en el horario
    """
    queryset = HorarioRango.objects.none()
    serializer_class = HorarioRangoSerializer


class DesignacionHorarioViewSet(viewsets.ModelViewSet):
    """
    ## Se designa un horario a un funcionario
    EL horario designado sera en un rango designado por una fecha de inicio y final
    """
    queryset = DesignacionHorario.objects.all()
    serializer_class = DesignacionHorarioSerializer


class RegistroHorarioViewSet(viewsets.ModelViewSet):
    """
    ## En este objeto se registran todos los Horarios
    Esta tabla es donde se registran todos los marcados realizados en los biometricos se realiza un sincronizacion
    de base de datos mediante un cliente rest
    """
    queryset = RegistroHorario.objects.all()
    serializer_class = RegistroHorarioSerializer


class FeriadoViewSet(viewsets.ModelViewSet):
    """
    ## En este objeto se aprueban los feriados
    Los feriados aprobados son antes sugeridos por el API REST de FERIADOS que entrega tentativamente todos los feriados del año
    """
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer


class TipoPermisoViewSet(viewsets.ModelViewSet):
    """
    ## En este objeto se definen los Tipos de Permiso
    Se definiran todos los tipos de permisos validos para el sistema
    """
    queryset = TipoPermiso.objects.all()
    serializer_class = TipoPermisoSerializer


class DesignacionPermisoViewSet(viewsets.ModelViewSet):
    """
    ## En esta tabla se designara un permiso y se aprobara el mismo
    Se designa un permiso y mediante un __token_mail__ se aprueba por el inmediato superior del funcionario, los datos del inmediato superior se
    consumen de una API REST de ORGANIGRAMA
    """
    queryset = DesignacionPermiso.objects.all()
    serializer_class = DesignacionPermisoSerializer
