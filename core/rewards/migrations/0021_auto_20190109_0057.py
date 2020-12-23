# Generated by Django 2.0.9 on 2019-01-09 00:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rewards', '0020_auto_20190108_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='name',
            field=models.CharField(choices=[('shove', 'Bet or raise all-in'), ('big_bluff', 'Win a 200bb+ pot without showdown with a bottom 20%% hand'), ('big_call', 'Call a 50bb+ bet on the river with a bottom 20%% hand, and win'), ('big_win', 'Win a 500bb+ pot'), ('run_bad', 'Lose 800bbs or more in a continuous session'), ('marathon', 'Play 500 hands in a continuous session'), ('hello_world', 'Filled out profile information'), ('nice_session', 'Win 800bbs or more in a continuous session'), ('dedicated', 'Play at least 5000 total hands'), ('adept', 'Play at least 10000 total hands'), ('the_teddy', 'Win with pocket aces against an Ax full house'), ('mike_mcd', 'Lose with an Ax full house against pocket aces '), ('its_a_trap', 'Check-raise all-in on the river, get called, and win'), ('cool_hand_luke', 'Win a 500bb+ pot with a bottom 5%% hand'), ('bombs_away', 'Win a 300bb+ pot without ever facing a bet or raise'), ('true_grit', 'Win a 500bb+ pot without ever betting or raising'), ('double_check_raise', 'Check-raise twice in the same hand and win the pot'), ('trifecta', 'Check-raise, check-raise, check-raise all-in and win'), ('quadfecta', 'Limp- or call-reraise, plus a trifecta'), ('soul_reader', 'Call on the river and win a pot with Jx or worse and no pair'), ('golden_week', 'Finish week {} in 1st place Season {}'), ('silver_week', 'Finish week {} in 2nd place Season {}'), ('bronze_week', 'Finish week {} in 3rd place Season {}'), ('golden_season', 'Finish Season {} in 1st place'), ('silver_season', 'Finish Season {} in 2nd place'), ('bronze_season', 'Finish Season {} in 3rd place'), ('season_top_5', 'Finish Season {} in top 5'), ('season_top_10', 'Finish Season {} in top 10'), ('season_one_percent', 'Finish Season {} in top 1%'), ('season_five_percent', 'Finish Season {} in top 5%'), ('badgelord', 'Finish Season in top 1% with most unique badges'), ('completed', 'Earn all the easily obtained badges'), ('black_hat', 'Attempt a technical exploit against Oddslingers'), ('potty_mouth', 'Attempted to use swear words on the site'), ('tourney_winner', 'Win a tournament'), ('the_duck', 'Win a 400bb+ pot with 72o at showdown'), ('quads', 'Win with four-of-a-kind'), ('straight_flush', 'Win with a straight flush at showdown'), ('steel_wheel', 'Win with an ace-to-5 straight flush at showdown'), ('royalty', 'Win with a royal flush at showdown'), ('champion', 'Win a tournament with at least 500 entrants'), ('because_it_is_there', 'Be the king-of-the-hill at the end of a week'), ('so_many_chips', 'Obtain a play-chip balance of 1,000,000 chips or more'), ('play_chip_diety', 'Obtain a play-chip balance of 9,999,999 chips or more'), ('heater', 'Win at least 1000 bbs in one session'), ('sizzler', 'Win 1500 bbs in a 24-hour period'), ('god_mode', 'Win at least 2000 bbs in one session'), ('bad_beat', 'Lose with aces-full (using both holecards) or better'), ('cooler', 'Lose 300bbs or more with top 0.1%% hand'), ('suckout', 'Win an all-in with 1%% equity'), ('hes_on_fire', 'Get all-in and win three times in a row'), ('this_is_rigged', 'Lose 1000bbs or more in a continuous session'), ('just_one_more_hand', 'Play 5,000 hands in a continuous session'), ('cant_stop_wont_stop', 'Play 10,000 hands in a continuous session and in at least 500bbs'), ('grinder', 'Play 50,000 hands in a month'), ('true_grinder', 'Play 100,000 hands in a month'), ('capital_g_grinder', 'Play the more hands than any other player in a month'), ('fiend', 'Play 500,000 hands in a 1-year period'), ('veteran', 'Play at least 100,000 total hands'), ('pro', 'Play at least 500,000 total hands'), ('seen_it_all', 'Play a total of 1,000,000 hands'), ('bug_hunter', 'Report a bug that gets fixed'), ('genesis', 'One of the first 1000 accounts'), ('fearless_leader', 'Open an account before 2019'), ('badgiest_badger', 'The player with the most badges'), ('king_of_the_hill', 'The biggest winner this week so far in KOTH points'), ('security_minded', 'Reviewed login history for suspicious activity'), ('good_samaritan', 'Manually awarded for recognized good behaviour'), ('streamer', 'Stream a session'), ('popular_streamer', 'Streamed play and got 100+ simultaneous viewers'), ('do_unto_others', 'Positive "handshake" balance')], db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='badge',
            name='season',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterIndexTogether(
            name='badge',
            index_together={('user', 'season')},
        ),
    ]