# Generated by Django 5.1.4 on 2024-12-11 20:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='release_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
