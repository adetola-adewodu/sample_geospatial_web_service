# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
    ]
