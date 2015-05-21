# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0003_auto_20150521_0759'),
    ]

    operations = [
        migrations.CreateModel(
            name='JefeDepartamento',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='Administrativo.Persona')),
                ('programa', models.OneToOneField(to='Administrativo.Programa')),
            ],
            bases=('Administrativo.persona',),
        ),
    ]
