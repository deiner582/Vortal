# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0003_auto_20150621_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculafinanciera',
            name='estado',
            field=models.CharField(default=b'Pendiente', max_length=10, null=True, blank=True, choices=[(b'Pagado', b'Pagado'), (b'Pendiente', b'Pendiente')]),
        ),
    ]
