# tournaments/models.py
from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

from django.db.models.signals import post_save
from django.dispatch import receiver


class Tournament(models.Model):
    game = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    start_time = models.TimeField()
    max_players = models.IntegerField()
    group_size = models.CharField(max_length=50, choices=[('solo', 'Solo'), ('duo', 'Duo'), ('squad', 'Squad')])

    def __str__(self):
        return self.name

class Slot(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    total_slots = models.PositiveIntegerField()
    booked_slots = models.PositiveIntegerField(default=0)

    def remaining_slots(self):
        remaining_slots = self.total_slots - self.booked_slots
        return remaining_slots

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=250,blank=True, null=True)
    player_1 = models.CharField(max_length=250,blank=True, null=True)
    player_2 = models.CharField(max_length=250,blank=True, null=True)
    player_3 = models.CharField(max_length=250,blank=True, null=True)
    player_4 = models.CharField(max_length=250,blank=True, null=True)
    player_1_bgmi_id = models.CharField(max_length=250,blank=True, null=True)
    player_2_bgmi_id = models.CharField(max_length=250,blank=True, null=True)
    player_3_bgmi_id = models.CharField(max_length=250,blank=True, null=True)
    player_4_bgmi_id = models.CharField(max_length=250,blank=True, null=True)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return self.team_name


@receiver(post_save, sender=Tournament)
def create_group_instance(sender, instance, created, **kwargs):
    if created:
        if instance.group_size == 'squad':
            Slot.objects.create(tournament=instance, total_slots=25)
        elif instance.group_size == 'duo':
            Slot.objects.create(tournament=instance, total_slots=50)
        elif instance.group_size == 'solo':
            Slot.objects.create(tournament=instance, total_slots=100)



class Room(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=255)
    room_pass = models.CharField(max_length=255)

    def __str__(self):
        return self.tournament.name
