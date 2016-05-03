from django.shortcuts import render

# ----------------------------------------------------------------------------------------------
# REST
# ----------------------------------------------------------------------------------------------
from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriados, TipoPermiso, DesignacionPermiso
from serializers import HorarioSerializer, HorarioRangoSerializer, DesignacionHorarioSerializer, RegistroHorarioSerializer, FeriadosSerializer, TipoPermisoSerializer, DesignacionPermisoSerializer
from rest_framework import viewsets
from permissions import HorarioPermission


# REST TABLES
class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = (HorarioPermission,)


class HorarioRangoViewSet(viewsets.ModelViewSet):
    queryset = HorarioRango.objects.none()
    serializer_class = HorarioRangoSerializer


class DesignacionHorarioViewSet(viewsets.ModelViewSet):
    queryset = DesignacionHorario.objects.all()
    serializer_class = DesignacionHorarioSerializer


class RegistroHorarioViewSet(viewsets.ModelViewSet):
    queryset = RegistroHorario.objects.all()
    serializer_class = RegistroHorarioSerializer


class FeriadosViewSet(viewsets.ModelViewSet):
    queryset = Feriados.objects.all()
    serializer_class = FeriadosSerializer


class TipoPermisoViewSet(viewsets.ModelViewSet):
    queryset = TipoPermiso.objects.all()
    serializer_class = TipoPermisoSerializer


class DesignacionPermisoViewSet(viewsets.ModelViewSet):
    queryset = DesignacionPermiso.objects.all()
    serializer_class = DesignacionPermisoSerializer
