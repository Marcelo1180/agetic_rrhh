# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_personal', '0008_auto_20160504_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designacionpermiso',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='designacionpermiso',
            name='hora_ini',
            field=models.TimeField(blank=True, null=True),
        ),
    ]