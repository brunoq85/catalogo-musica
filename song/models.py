import uuid
from django.db import models


class Song(models.Model):
    id_song = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()

    class Meta:
        db_table = "song"
        ordering = ['artist']
        verbose_name_plural = "songs"

    def __str__(self):
        return self.title
