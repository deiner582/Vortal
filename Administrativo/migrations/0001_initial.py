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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('nombre', models.CharField(max_length=2, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
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
            name='Hora',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('dia', models.CharField(max_length=20, choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'), (b'Viernes', b'viernes'), (b'Sabado', b'Sabado')])),
                ('horainicio', models.TimeField()),
                ('horafinal', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioAula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aula', models.ForeignKey(to='Administrativo.Aula')),
                ('hora', models.ForeignKey(to='Administrativo.Hora')),
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
                ('tipo_documento', models.CharField(max_length=20, choices=[(b'C.C', b'Cedula de ciudadania'), (b'T.I', b'Tarjeta de identidad'), (b'C.E', b'Cedula Extranjera'), (b'Registro Civil', b'Registro Civil')])),
                ('documento', models.IntegerField(serialize=False, primary_key=True)),
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
        migrations.CreateModel(
            name='JefeDepartamento',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Administrativo.Persona')),
                ('programa', models.OneToOneField(to='Administrativo.Programa')),
            ],
            bases=('Administrativo.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='lugar_expedicion',
            field=models.ForeignKey(related_name='expedicion', to='Administrativo.Ciudad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='lugar_nacimiento',
            field=models.ForeignKey(related_name='nacimiento', to='Administrativo.Ciudad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pensum',
            name='programa',
            field=models.ForeignKey(to='Administrativo.Programa'),
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
        migrations.AlterUniqueTogether(
            name='horarioaula',
            unique_together=set([('hora', 'aula')]),
        ),
        migrations.AlterUniqueTogether(
            name='aula',
            unique_together=set([('bloque', 'nombre')]),
        ),
    ]
