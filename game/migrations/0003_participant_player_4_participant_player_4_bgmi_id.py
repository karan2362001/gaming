# Generated by Django 5.0.3 on 2024-03-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_participant_is_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='player_4',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='player_4_bgmi_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
