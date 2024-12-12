from django.db import models
from django.urls import reverse


class Travel(models.Model):
    destination_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    popular_season = models.CharField(max_length=100)

    def get_delete_url(self):
        return reverse('travels:delete', args=[self.pk])

    def get_detail_url(self):
        return reverse('travels:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('travels:update', args=[self.pk])
