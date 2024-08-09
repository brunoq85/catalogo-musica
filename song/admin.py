from django.contrib import admin
from song.models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('id_song', 'title', 'artist', 'album', 'genre', 'release_year')
    search_fields = ('title', 'artist', 'album', 'genre', 'release_year')

admin.site.register(Song, SongAdmin)
