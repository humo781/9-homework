from django.db import models
from django.urls import reverse
from django.utils import timezone


class Sport(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

    def get_delete_url(self):
        return reverse('sports:delete', args=[self.pk])

    def get_detail_url(self):
        return reverse('sports:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('sports:update', args=[self.pk])
