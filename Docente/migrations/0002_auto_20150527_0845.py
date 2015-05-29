# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='grupo',
            table='Grupo',
        ),
    ]
