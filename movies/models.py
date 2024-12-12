from django.db import models
from django.urls import reverse
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.DateField(default=timezone.now)

    def get_delete_url(self):
        return reverse('movies:delete', args=[self.pk])

    def get_detail_url(self):
        return reverse('movies:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('movies:update', args=[self.pk])
