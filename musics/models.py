from django.db import models
from django.urls import reverse
from django.utils import timezone


class Music(models.Model):
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now)

    def get_delete_url(self):
        return reverse('musics:delete', args=[self.pk])

    def get_detail_url(self):
        return reverse('musics:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('musics:update', args=[self.pk])
