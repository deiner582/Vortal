# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0004_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota_final',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
