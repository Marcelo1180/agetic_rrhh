# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control_personal', '0006_auto_20160503_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrohorario',
            name='funcionario',
        ),
    ]