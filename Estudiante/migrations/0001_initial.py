# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0003_auto_20150521_0759'),
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
