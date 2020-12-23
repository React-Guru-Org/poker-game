# Generated by Django 2.0.7 on 2018-07-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0019_merge_20180726_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sit_behaviour_int',
            field=models.IntegerField(choices=[(2, 'SITTING_OUT'), (5, 'SIT_IN_AT_BLINDS_PENDING'), (3, 'SIT_IN_PENDING')], default=2),
        ),
    ]