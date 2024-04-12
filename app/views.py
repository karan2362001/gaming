from django.shortcuts import render,get_object_or_404,redirect
from game.models import *
from django.utils import timezone
from game import models
from django.contrib.auth.models import User
from .models import Contact
from django.contrib import messages

def index(request):
    user_tournament = Tournament.objects.all()
    # Filter past tournaments
    past_tournaments = user_tournament.filter(start_date__lt=timezone.now())

    # Filter upcoming tournaments
    upcoming_tournaments = user_tournament.filter(start_date__gte=timezone.now())
    context = {
        'user_tournament':user_tournament,
        'past_tournaments': past_tournaments,
        'upcoming_tournaments': upcoming_tournaments
    }
    return render(request,'user/index.html',context)

def about(request):
    return render(request,'user/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contacts = Contact(name=name,email=email,message=message)
        contacts.save()
        messages.success(request,'Thank you for Your response')
        return redirect('index')
    return render(request,'user/contact.html')

def tournament(request):
    user_tournament = Tournament.objects.all()

     # Filter past tournaments
    past_tournaments = user_tournament.filter(start_date__lt=timezone.now())

    # Filter upcoming tournaments
    upcoming_tournaments = user_tournament.filter(start_date__gte=timezone.now())

    for tournament in past_tournaments:
        winner = Participant.objects.filter(tournament=tournament, is_winner=True).first()
        if winner:
            winners = winner.team_name
    context = {
        'user_tournament':user_tournament,
        'past_tournaments': past_tournaments,
        'upcoming_tournaments': upcoming_tournaments,
        'winner':winners
    }
    return render(request,'user/tournament.html',context)


def User_Dashboard(request):
        
    user_participations = Participant.objects.filter(user=request.user)

    userprofile = get_object_or_404(User, username=request.user)

    context = {
        'user_participations':user_participations,
        'user':userprofile
    }
    return render(request,'user/user_dashboard.html',context)