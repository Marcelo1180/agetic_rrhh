from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriados, TipoPermiso, DesignacionPermiso
from rest_framework import serializers


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario


class HorarioRangoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioRango


class DesignacionHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignacionHorario


class RegistroHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHorario


class FeriadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feriados


class TipoPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPermiso


class DesignacionPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignacionPermiso
