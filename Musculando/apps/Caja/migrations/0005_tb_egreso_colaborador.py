# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-14 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Colaboradores', '0007_tb_cuentacolaborador'),
        ('Caja', '0004_tb_egreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_egreso',
            name='colaborador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Colaboradores.tb_colaboradores'),
        ),
    ]
