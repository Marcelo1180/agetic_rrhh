from models import Funcionario, Horario, HorarioRango, DesignacionHorario, RegistroHorario, Feriado, TipoPermiso, DesignacionPermiso
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


class FeriadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feriado
        

class TipoPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPermiso


class DesignacionPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignacionPermiso
