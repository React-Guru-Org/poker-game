# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-02 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0006_auto_20170630_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='ip',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='user_agent',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
