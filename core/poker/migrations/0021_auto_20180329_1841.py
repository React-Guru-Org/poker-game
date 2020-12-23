# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-29 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0020_merge_20180129_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handhistoryevent',
            name='event',
            field=models.CharField(choices=[('DEAL', 'DEAL'), ('POST', 'POST'), ('POST_DEAD', 'POST_DEAD'), ('ANTE', 'ANTE'), ('BET', 'BET'), ('RAISE_TO', 'RAISE_TO'), ('CALL', 'CALL'), ('CHECK', 'CHECK'), ('FOLD', 'FOLD'), ('BUY', 'BUY'), ('TAKE_SEAT', 'TAKE_SEAT'), ('LEAVE_SEAT', 'LEAVE_SEAT'), ('SIT_IN', 'SIT_IN'), ('SIT_OUT', 'SIT_OUT'), ('WIN', 'WIN'), ('RETURN_CHIPS', 'RETURN_CHIPS'), ('OWE_SB', 'OWE_SB'), ('OWE_BB', 'OWE_BB'), ('SET_BLIND_POS', 'SET_BLIND_POS'), ('NEW_HAND', 'NEW_HAND'), ('NEW_STREET', 'NEW_STREET'), ('POP_CARDS', 'POP_CARDS'), ('UPDATE_STACK', 'UPDATE_STACK'), ('SIT_IN_AT_BLINDS', 'SIT_IN_AT_BLINDS'), ('SIT_OUT_AT_BLINDS', 'SIT_OUT_AT_BLINDS'), ('SET_AUTO_REBUY', 'SET_AUTO_REBUY'), ('CREATE_TRANSFER', 'CREATE_TRANSFER'), ('ADD_ORBIT_SITTING_OUT', 'ADD_ORBIT_SITTING_OUT'), ('END_HAND', 'END_HAND'), ('SET_TIMEBANK', 'SET_TIMEBANK'), ('RECORD_ACTION', 'RECORD_ACTION'), ('CHAT', 'CHAT'), ('NOTIFICATION', 'NOTIFICATION'), ('SET_BOUNTY_FLAG', 'SET_BOUNTY_FLAG'), ('REVEAL_HAND', 'REVEAL_HAND'), ('DELAY_COUNTDOWN', 'DELAY_COUNTDOWN'), ('RESET', 'RESET'), ('SET_PRESET_CHECKFOLD', 'SET_PRESET_CHECKFOLD'), ('SET_PRESET_CHECK', 'SET_PRESET_CHECK'), ('SET_PRESET_CALL', 'SET_PRESET_CALL'), ('MUCK', 'MUCK'), ('WAIT_TO_SIT_IN', 'WAIT_TO_SIT_IN'), ('SHOWDOWN_COMPLETE', 'SHOWDOWN_COMPLETE'), ('BOUNTY_WIN', 'BOUNTY_WIN')], max_length=64, null=True),
        ),
    ]
