from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from app.models import *

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    tournament_count = Tournament.objects.all().count()
    player_count = Participant.objects.all().count()

    context = {
        'tournament_count':tournament_count,
        'player_count':player_count,
    }
    return render(request,'admin/index.html',context)

@login_required(login_url='login')
def admin_tournament(request):
    tournaments = Tournament.objects.all()
    context = {
        'tournaments':tournaments,
    }
    return render(request,'admin/tournament.html',context)

@login_required(login_url='login')
def winner(request,wid):
    Participant.objects.filter(id=wid).update(is_winner=True)
    return redirect('admin_tournament')  # Redirect to admin dashboard or desired page


@login_required(login_url='login')
def Add_Tournament(request):
    if request.method == 'POST':
        game = request.POST.get('game')
        name = request.POST.get('game_name')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        max_players = request.POST.get('max_players')
        group_size = request.POST.get('group_size')

        tournament_query = Tournament(game=game,name=name,start_date=start_date,start_time=start_time,max_players=max_players,group_size=group_size)
        tournament_query.save()
        messages.success(request, 'Tournament Created successfully!')
        
        return redirect('admin_tournament')
    return render(request,'admin/tournament.html')

@login_required(login_url='login')
def admin_slot(request):
    slot = Slot.objects.all()

    context = {
        'slot':slot
    }
    return render(request,'admin/slot.html',context)

@login_required(login_url='login')
def room(request):
    room = Room.objects.all()
    tournaments_id = Tournament.objects.all()

    context = {
        'room':room,
        'tournaments':tournaments_id,
    }
    return render(request,'admin/room.html',context)


@login_required(login_url='login')
def Add_Room(request):
    if request.method == 'POST':
        tournament_id = request.POST.get('tournament')
        room_id = request.POST.get('room_id')
        room_pass = request.POST.get('room_pass')

        tournament = get_object_or_404(Tournament, id=tournament_id)


        room_query = Room(tournament=tournament,room_id=room_id,room_pass=room_pass)
        room_query.save()
        messages.success(request, 'Room Created successfully!')
        return redirect('room')
    return render(request,'admin/room.html')


@login_required(login_url='login')
def Player(request):
    player = Participant.objects.all()


    context = {
        'player':player,
    }
    return render(request,'admin/player.html',context)


def Tournament_Detail(request,tid):

    tournament_detail = Tournament.objects.get(id=tid)
    tournament_slot = Slot.objects.get(tournament=tid)

    context = {
        'tournament_detail':tournament_detail,
        'tournament_slot':tournament_slot,
    }

    return render(request,'user/tournament_detail.html',context)

@login_required(login_url='login')
def Join_Tournament(request):
    user = request.user
    if request.method == 'POST':
        tournament_id = request.POST.get('tournament_id')
        team_name = request.POST.get('team_name')
        player_1 = request.POST.get('player_1')
        player_2 = request.POST.get('player_2')
        player_3 = request.POST.get('player_3')
        player_4 = request.POST.get('player_4')
        player_1_bgmi_id = request.POST.get('player_1_bgmi_id')
        player_2_bgmi_id = request.POST.get('player_2_bgmi_id')
        player_3_bgmi_id = request.POST.get('player_3_bgmi_id')
        player_4_bgmi_id = request.POST.get('player_4_bgmi_id')

        tournament = get_object_or_404(Tournament, id=tournament_id)

        # Check if the user has already joined the tournament
        if Participant.objects.filter(user=user, tournament=tournament).exists():
            messages.success(request, 'You Alredy Joined This Tournament')
            return redirect('User_Dashboard')

        # Check if there are remaining slots
        slot_mod = Slot.objects.get(tournament=tournament)
        if slot_mod.remaining_slots() <= 0:
            messages.success(request, 'This Tournament is Full. Try With Other Tournamrent!')
            return redirect('tournament')

        join_tournament_query = Participant(
            user=user,
            tournament=tournament,
            team_name=team_name,
            player_1=player_1,
            player_2=player_2,
            player_3=player_3,
            player_4=player_4,
            player_1_bgmi_id=player_1_bgmi_id,
            player_2_bgmi_id=player_2_bgmi_id,
            player_3_bgmi_id=player_3_bgmi_id,
            player_4_bgmi_id=player_4_bgmi_id)

        slot_mod = Slot.objects.get(tournament=tournament)
        slot_mod.booked_slots += 1
        slot_mod.save()
        join_tournament_query.save()

        messages.success(request, 'Successfully Register The Tournament.')
        return redirect('tournament')
    return render(request,'user/tournament.html')


@login_required(login_url='login')
def edit_tournament(request,id):
    tournament = Tournament.objects.get(id=id)
    context = {
        'tournament':tournament,
    }
    return render(request,'admin/update_tournament.html',context)


@login_required(login_url='login')
def admin_edit_tournament(request,tid):
    if request.method == 'POST':
        game = request.POST.get('game')
        name = request.POST.get('game_name')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        max_players = request.POST.get('max_players')
        group_size = request.POST.get('group_size')

        update_tourn = Tournament.objects.get(id=tid)
        update_tourn.game=game
        update_tourn.name=name
        update_tourn.start_date=start_date
        update_tourn.start_time=start_time
        update_tourn.max_players=max_players
        update_tourn.group_size=group_size
        update_tourn.save()
        messages.success(request, 'Tournament Updated successfully!')

        return redirect('admin_tournament')
    return render(request,'admin/update_tournament.html')


@login_required(login_url='login')
def edit_room(request,id):
    room = Room.objects.get(id=id)
    tournament = Tournament.objects.all()
    context = {
        'room':room,
        'tournament':tournament
    }
    return render(request,'admin/update_room.html',context)

@login_required(login_url='login')
def admin_edit_room(request, roomid):
    if request.method == 'POST':
        tournament_id = request.POST.get('tournament')
        room_id = request.POST.get('room_id')
        room_pass = request.POST.get('room_pass')

        tournament = Tournament.objects.get(id=tournament_id)


        room_update = Room.objects.get(id=roomid)
        room_update.tournament=tournament
        room_update.room_id=room_id
        room_update.room_pass=room_pass
        room_update.save()
        messages.success(request, 'Room Updated successfully!')

        return redirect('room')
    return None



@login_required(login_url='login')
def Admin_contact(request):
    contact = Contact.objects.all()
    context = {
        'contact':contact
    }
    return render(request,'admin/admin_contact.html',context)