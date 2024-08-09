from django.contrib import admin
from django.urls import path
from song.views import list_song_views


urlpatterns = [
    path('song/', list_song_views, name='song'),
]