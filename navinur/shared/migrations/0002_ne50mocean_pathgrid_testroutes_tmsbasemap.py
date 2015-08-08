# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
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
        migrations.CreateModel(
            name='PathGrid',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=32616, null=True, blank=True)),
            ],
            options={
                'db_table': 'path_grid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TmsBasemap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'db_table': 'tms_basemap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestRoutes',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('start', models.CharField(max_length=150)),
                ('end', models.CharField(max_length=150)),
                ('distance', models.DecimalField(null=True, max_digits=1000, decimal_places=5, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326, null=True, blank=True)),
            ],
            options={
                'db_table': 'test_routes',
                'managed': True,
            },
        ),
    ]
