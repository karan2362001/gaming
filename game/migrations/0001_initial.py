# Generated by Django 5.0.3 on 2024-03-24 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('max_players', models.IntegerField()),
                ('group_size', models.CharField(choices=[('solo', 'Solo'), ('duo', 'Duo'), ('squad', 'Squad')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Solo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_slots', models.PositiveIntegerField()),
                ('booked_slots', models.PositiveIntegerField(default=0)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.CharField(max_length=255)),
                ('room_pass', models.CharField(max_length=255)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=250, null=True)),
                ('player_1', models.CharField(blank=True, max_length=250, null=True)),
                ('player_2', models.CharField(blank=True, max_length=250, null=True)),
                ('player_3', models.CharField(blank=True, max_length=250, null=True)),
                ('player_1_bgmi_id', models.CharField(blank=True, max_length=250, null=True)),
                ('player_2_bgmi_id', models.CharField(blank=True, max_length=250, null=True)),
                ('player_3_bgmi_id', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Duo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.tournament')),
            ],
        ),
    ]
