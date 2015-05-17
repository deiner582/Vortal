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
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Administrativo.Persona')),
                ('profesion', models.ForeignKey(to='Docente.Profesion')),
            ],
            bases=('Administrativo.persona',),
        ),
    ]
