# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_personal', '0004_auto_20160503_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariorango',
            name='tolerancia_individual',
            field=models.IntegerField(default=0, help_text='Trabajar con el modo de tolerancia acumulada'),
        ),
    ]
