# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-06 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Socios', '0016_tb_socio_tarifadiaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_socio',
            name='IsDiario',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tb_socio',
            name='IsMensualAnual',
            field=models.BooleanField(default=False),
        ),
    ]
