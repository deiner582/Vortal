# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0002_auto_20150629_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculaacademica',
            name='estudiante',
            field=models.ForeignKey(to='Estudiante.Estudiante'),
        ),
        migrations.AlterField(
            model_name='matriculaacademica',
            name='grupos',
            field=models.ForeignKey(to='Docente.Grupo'),
        ),
        migrations.AlterUniqueTogether(
            name='matriculaacademica',
            unique_together=set([('estudiante', 'grupos')]),
        ),
    ]
