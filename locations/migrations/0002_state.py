# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 19:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('ogc_fid', models.IntegerField(primary_key=True, serialize=False)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('geo_id', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('lsad', models.CharField(max_length=200)),
                ('censusarea', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
    ]