# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Administrativo.Persona')),
            ],
            bases=('Administrativo.persona',),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grupo', models.IntegerField()),
                ('horario', models.ManyToManyField(to='Administrativo.HorarioAula')),
                ('materia', models.ForeignKey(to='Administrativo.Materia')),
                ('profesor', models.ForeignKey(to='Docente.Docente')),
            ],
            options={
                'db_table': 'Grupo',
            },
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Profesiones',
            },
        ),
        migrations.AddField(
            model_name='docente',
            name='profesion',
            field=models.ForeignKey(to='Docente.Profesion'),
        ),
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together=set([('grupo', 'materia')]),
        ),
    ]
