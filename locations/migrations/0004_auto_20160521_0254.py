# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_ndharea'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ndharea',
            new_name='Nhdarea',
        ),
    ]