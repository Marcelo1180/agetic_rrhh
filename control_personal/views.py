#!/usr/bin/python
# -*- coding: utf8 -*-

from django.shortcuts import render

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
    ## Establecer un Horario para una funcionario
    Definir un Nombre de horario

    __sw_tolerancia_acumulada__ La tolerancia acumulada es la tolerancia para un dia
    """
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    # permission_classes = (HorarioPermission,)


class HorarioRangoViewSet(viewsets.ModelViewSet):
    queryset = HorarioRango.objects.none()
    serializer_class = HorarioRangoSerializer


class DesignacionHorarioViewSet(viewsets.ModelViewSet):
    queryset = DesignacionHorario.objects.all()
    serializer_class = DesignacionHorarioSerializer


class RegistroHorarioViewSet(viewsets.ModelViewSet):
    queryset = RegistroHorario.objects.all()
    serializer_class = RegistroHorarioSerializer


class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = Feriado.objects.all()
    serializer_class = FeriadoSerializer


class TipoPermisoViewSet(viewsets.ModelViewSet):
    queryset = TipoPermiso.objects.all()
    serializer_class = TipoPermisoSerializer


class DesignacionPermisoViewSet(viewsets.ModelViewSet):
    queryset = DesignacionPermiso.objects.all()
    serializer_class = DesignacionPermisoSerializer
