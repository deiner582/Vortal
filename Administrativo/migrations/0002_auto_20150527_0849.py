# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='facultad',
            table='Facultad',
        ),
        migrations.AlterModelTable(
            name='materia',
            table='Materia',
        ),
        migrations.AlterModelTable(
            name='programa',
            table='Programa',
        ),
    ]
