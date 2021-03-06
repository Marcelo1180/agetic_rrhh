# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 22:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control_personal', '0005_auto_20160503_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designacionhorario',
            name='funcionario',
        ),
        migrations.AddField(
            model_name='designacionhorario',
            name='fecha_fin',
            field=models.DateField(default="2016-04-06"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designacionhorario',
            name='fecha_ini',
            field=models.DateField(default="2016-04-06"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designacionhorario',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='horariorango',
            name='tolerancia_individual',
            field=models.IntegerField(default=0, help_text='Si el modo de tolerancia acumulada se encuentra desactivada puede utilizar este tipo de tolerancia, caso contrario dejar en 0'),
        ),
    ]
