# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-27 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Colaboradores', '0008_auto_20180618_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_cuentacolaborador',
            name='typePago',
            field=models.CharField(choices=[('honorarios Mensuales', 'Honorarios Mensuales'), ('Monto Por Clase', 'Monto Por clase'), ('Sin Definir', 'Sin Definir'), ('Comision Por Clase', 'Comision Por Clase'), ('Presentimo', 'Presentimo'), ('Aguinaldo', 'Aguinaldo'), ('Liquidacion Mensual', 'Liquidacion Mensual')], default='SinDefinir', max_length=300),
        ),
    ]
