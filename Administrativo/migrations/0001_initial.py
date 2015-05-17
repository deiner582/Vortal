# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('nombre', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Facultades',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('grupo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('dia', models.CharField(max_length=20, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'viernes'), (b'Sabado', b'Sabado')])),
                ('horainicio', models.TimeField()),
                ('horafinal', models.TimeField()),
                ('aula', models.ForeignKey(to='Administrativo.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('prerequisito', models.ForeignKey(related_name='materia', blank=True, to='Administrativo.Materia', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pensum',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('creditos', models.IntegerField()),
                ('materias', models.ManyToManyField(to='Administrativo.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('documento', models.IntegerField(serialize=False, primary_key=True)),
                ('tipo_documento', models.CharField(max_length=20, choices=[(b'C.C', b'Cedula de ciudadania'), (b'T.I', b'Tarjeta de identidad'), (b'C.E', b'Cedula Extranjera'), (b'Registro Civil', b'Registro Civil')])),
                ('fecha_expedicion', models.DateField()),
                ('primer_nombre', models.CharField(max_length=30)),
                ('segundo_nombre', models.CharField(max_length=30, null=True, blank=True)),
                ('primer_apellido', models.CharField(max_length=30)),
                ('segundo_apellido', models.CharField(max_length=30, null=True, blank=True)),
                ('sexo', models.CharField(default=b'F', max_length=1, choices=[(b'M', b'M'), (b'F', b'F')])),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('lugar_expedicion', models.ForeignKey(related_name='expedicion', to='Administrativo.Ciudad')),
                ('lugar_nacimiento', models.ForeignKey(related_name='nacimiento', to='Administrativo.Ciudad')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('facultad', models.ForeignKey(to='Administrativo.Facultad')),
            ],
        ),
        migrations.AddField(
            model_name='pensum',
            name='programa',
            field=models.ForeignKey(to='Administrativo.Programa'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='horas',
            field=models.ManyToManyField(to='Administrativo.Hora'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='materia',
            field=models.ForeignKey(to='Administrativo.Materia'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='Administrativo.Departamento'),
        ),
        migrations.AddField(
            model_name='aula',
            name='bloque',
            field=models.ForeignKey(to='Administrativo.Bloque'),
        ),
    ]
