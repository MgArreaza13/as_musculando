# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-23 13:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Configuracion', '0005_tb_tipoegreso'),
        ('Caja', '0003_auto_20180315_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField(default='0000', null=True)),
                ('descripcion', models.TextField(default='Sin Descripcion', max_length=3000, null=True)),
                ('dateCreate', models.DateField(auto_now=True)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Proveedores.tb_proveedor')),
                ('tipoDeEgreso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Configuracion.tb_tipoEgreso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
                'db_table': 'egresos',
            },
        ),
    ]
