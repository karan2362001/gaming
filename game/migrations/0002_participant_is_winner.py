# Generated by Django 5.0.3 on 2024-03-25 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='is_winner',
            field=models.BooleanField(default=False),
        ),
    ]
