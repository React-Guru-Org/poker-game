# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-18 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poker', '0021_auto_20180329_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokertournament',
            name='chat_history',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poker.ChatHistory'),
        ),
        migrations.AddField(
            model_name='pokertournament',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokertournament',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pokertournament',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pokertournament',
            name='status',
            field=models.IntegerField(choices=[(1, 'PENDING'), (2, 'STARTED'), (3, 'FINISHED')], default=1),
        ),
        migrations.AlterField(
            model_name='freezeout',
            name='max_entrants',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='player',
            name='playing_state_int',
            field=models.IntegerField(choices=[(1, 'SITTING_IN'), (2, 'SITTING_OUT'), (3, 'SIT_IN_PENDING'), (4, 'SIT_OUT_PENDING'), (5, 'SIT_IN_AT_BLINDS_PENDING'), (6, 'LEAVE_SEAT_PENDING'), (7, 'DISCONNECTED'), (8, 'TOURNEY_SITTING_OUT')], null=True),
        ),
        migrations.AlterField(
            model_name='pokertable',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poker.Freezeout'),
        ),
        migrations.AlterField(
            model_name='pokertournament',
            name='buyin_amt',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=20),
        ),
        migrations.AlterField(
            model_name='pokertournament',
            name='entrants',
            field=models.ManyToManyField(related_name='tournaments', related_query_name='tournament', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pokertournament',
            name='name',
            field=models.CharField(default='Tournament', max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='pokertournament',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentresult',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', related_query_name='result', to='poker.PokerTournament'),
        ),
    ]
