# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidebets', '0002_auto_20180410_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebet',
            name='rebuys',
        ),
        migrations.AddField(
            model_name='sidebet',
            name='from_rebuy',
            field=models.BooleanField(default=False),
        ),
    ]
