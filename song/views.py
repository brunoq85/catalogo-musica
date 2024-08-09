from django.shortcuts import render
from song.models import Song


def list_song_views(request):
    songs = Song.objects.all().order_by('artist')
    artist = request.GET.get('artist')

    if(artist):
        songs = Song.objects.filter(artist__contains=artist)

    return render(request, template_name='song.html', context={'songs': songs})
