from django.urls import path
from app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('tournament',views.tournament,name='tournament'),
    path('User_Dashboard',views.User_Dashboard,name='User_Dashboard'),
]
