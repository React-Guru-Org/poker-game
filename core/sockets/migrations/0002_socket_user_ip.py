# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='user_ip',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
