# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_auto_20150803_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testroutes',
            name='geom',
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326, null=True, blank=True),
        ),
    ]
