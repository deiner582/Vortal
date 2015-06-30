# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculaacademica',
            name='estudiante',
            field=models.ForeignKey(blank=True, to='Estudiante.Estudiante', null=True),
        ),
        migrations.AlterField(
            model_name='matriculaacademica',
            name='grupos',
            field=models.ForeignKey(blank=True, to='Docente.Grupo', null=True),
        ),
    ]
