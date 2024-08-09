from django import forms
from song.models import Song


class SongModelForm(forms.ModelForm):
    model = Song
    fields = ['title', 'artist', 'album', 'genre', 'release_year']