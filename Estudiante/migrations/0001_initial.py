# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
        ('Docente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Administrativo.Persona')),
                ('estrato', models.CharField(default=1, max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')])),
                ('estado', models.CharField(default=b'Inscripto', max_length=9, null=True, blank=True, choices=[(b'Admitido', b'Admitido'), (b'Inscripto', b'Inscripto'), (b'Activo', b'Activo'), (b'Inactivo', b'Inactivo'), (b'PFU', b'PFU')])),
            ],
            bases=('Administrativo.persona',),
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MatriculaAcademica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estudiante', models.ForeignKey(to='Estudiante.Estudiante')),
                ('grupos', models.ForeignKey(to='Docente.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='MatriculaFinanciera',
            fields=[
                ('referencia', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('descuento', models.FloatField()),
                ('ano', models.DateField()),
                ('periodo', models.CharField(max_length=2, choices=[(b'1', b'1'), (b'2', b'2')])),
                ('estado', models.CharField(default=b'Pendiente', max_length=10, null=True, blank=True, choices=[(b'Pagado', b'Pagado'), (b'Pendiente', b'Pendiente')])),
                ('estudiante', models.ForeignKey(to='Estudiante.Estudiante')),
                ('precio', models.ForeignKey(to='Administrativo.PrecioMatricula')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='etnia',
            field=models.ForeignKey(default=b'Ninguna', to='Estudiante.Etnia'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(to='Administrativo.Programa'),
        ),
    ]
