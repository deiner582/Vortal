# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0003_preciomatricula'),
        ('Estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculaFinanciera',
            fields=[
                ('referencia', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('descuento', models.FloatField()),
                ('ano', models.TimeField()),
                ('periodo', models.CharField(max_length=2, choices=[(b'1', b'1'), (b'2', b'2')])),
                ('estudiante', models.ForeignKey(to='Estudiante.Estudiante')),
                ('precio', models.ForeignKey(to='Administrativo.PrecioMatricula')),
            ],
        ),
    ]
