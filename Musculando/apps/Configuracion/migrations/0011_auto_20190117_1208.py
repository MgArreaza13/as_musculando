# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-17 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Configuracion', '0010_tb_tipohorario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_turn_sesion',
            name='nameturnsession',
            field=models.CharField(default='', max_length=30),
        ),
    ]
