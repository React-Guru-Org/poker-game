# Generated by Django 2.0.8 on 2018-10-29 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0032_auto_20181018_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_playbyplay',
            field=models.BooleanField(default=True),
        ),
    ]
