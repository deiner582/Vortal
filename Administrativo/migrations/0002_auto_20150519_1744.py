# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
    ]
