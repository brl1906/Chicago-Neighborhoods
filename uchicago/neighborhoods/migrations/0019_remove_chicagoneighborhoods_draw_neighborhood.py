# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-01 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborhoods', '0018_landingpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chicagoneighborhoods',
            name='draw_neighborhood',
        ),
    ]
