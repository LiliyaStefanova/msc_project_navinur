# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_ne50mocean_pathgrid_testroutes_tmsbasemap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testroutes',
            name='distance',
            field=models.DecimalField(null=True, max_digits=1000, decimal_places=5, blank=True),
        ),
    ]
