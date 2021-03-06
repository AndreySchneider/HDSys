# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-28 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hdsysapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hdsysuser',
            name='position',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42, null=True),
        ),
        migrations.AlterField(
            model_name='hdsysuser',
            name='cpf',
            field=models.PositiveIntegerField(error_messages={'unique': 'Este CPF já está cadastrado no sistema. Insira um CPF diferente.'}, unique=True),
        ),
        migrations.AlterField(
            model_name='hdsysuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Este e-mail já está cadastrado no sistema. Insira um e-mail diferente.'}, max_length=75, unique=True),
        ),
        migrations.AlterField(
            model_name='hdsysuser',
            name='username',
            field=models.CharField(db_index=True, error_messages={'unique': 'Este nome de usuário já está cadastrado no sistema. Insira um nome de usuário diferente.'}, max_length=50, unique=True),
        ),
    ]
