# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0002_auto_20150527_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioMatricula',
            fields=[
                ('codigo', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('precio', models.FloatField()),
                ('facultad', models.ForeignKey(to='Administrativo.Facultad')),
            ],
        ),
    ]
