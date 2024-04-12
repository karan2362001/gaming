from django.urls import path
from game import views


urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('admin_tournament',views.admin_tournament,name='admin_tournament'),
    path('room',views.room,name='room'),
    path('Player',views.Player,name='Player'),
    path('Add_Tournament',views.Add_Tournament,name='Add_Tournament'),
    path('Add_Room',views.Add_Room,name='Add_Room'),
    path('Tournament_Detail/<int:tid>/',views.Tournament_Detail,name='Tournament_Detail'),
    path('Join_Tournament',views.Join_Tournament,name='Join_Tournament'),
    path('admin_slot',views.admin_slot,name='admin_slot'),

    path('winner/<int:wid>',views.winner,name='winner'),

  
    # Update Room
    path('edit_room/<int:id>/',views.edit_room,name='edit_room'),
    path('admin_edit_room/<int:roomid>/',views.admin_edit_room,name='admin_edit_room'),

    # Update Tournament
    path('edit_tournament/<int:id>/',views.edit_tournament,name='edit_tournament'),
    path('admin_edit_tournament/<int:tid>/',views.admin_edit_tournament,name='admin_edit_tournament'),

    path('Admin_contact',views.Admin_contact,name='Admin_contact'),

]


