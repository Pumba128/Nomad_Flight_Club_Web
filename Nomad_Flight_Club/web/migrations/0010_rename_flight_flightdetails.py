# Generated by Django 4.1.4 on 2022-12-27 20:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0009_flight_slug_flight_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Flight',
            new_name='FlightDetails',
        ),
    ]
