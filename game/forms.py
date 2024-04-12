# forms.py
from django import forms
from .models import Tournament,Room

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['game','name','start_date','start_time','max_players','group_size']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['tournament','room_id','room_pass']