# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ne50MOcean',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('scalerank', models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)),
                ('featurecla', models.CharField(max_length=32, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326, null=True, blank=True)),
            ],
            options={
                'db_table': 'ne_50m_ocean',
                'managed': False,
            },
        ),
    ]
