# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0003_auto_20150629_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota_1', models.FloatField()),
                ('nota_2', models.FloatField()),
                ('nota_3', models.FloatField()),
                ('nota_final', models.FloatField()),
                ('matriculaacedemica', models.ForeignKey(to='Estudiante.MatriculaAcademica')),
            ],
        ),
    ]
