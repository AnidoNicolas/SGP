# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
            ],
        ),
    ]
