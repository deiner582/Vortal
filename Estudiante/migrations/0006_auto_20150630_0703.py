# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0005_auto_20150629_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota_1',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_2',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='nota',
            name='nota_3',
            field=models.FloatField(default=0.0, null=True, blank=True),
        ),
    ]
