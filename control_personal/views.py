#!/usr/bin/python
# -*- coding: utf8 -*-

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
    """
    Cabecera y ruta:

# Header 3

```sh
asdfasdf
```
Parámetros de entrada y salida:

| Tipo | Parámetro    | Descripcion |
| --- | --- | --- |
| Entrada | `asunto` | Referencia de la hoja de ruta (generalmente la referencia es del primer documento) |
| Entrada | `comentario` | Comentario adicional referente al envio realizado |
| Entrada | `remitente` | Codigo de persona "encargado de recepcionar". La primera persona del ministerio de educacion al cual se envia el tramite |
| Entrada | `destinatario` | Codigo de persona "a quien va dirigido el documento" |
| Entrada | `fecha_limite_` | Fecha limite para atencion de la hoja de ruta por parte del destinatario |
| Entrada | `ipx` | Ip del equipo que genera la consulta |
| Salida | objeto json | La petición genera un objeto de insercion en formato json. |
    """
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
