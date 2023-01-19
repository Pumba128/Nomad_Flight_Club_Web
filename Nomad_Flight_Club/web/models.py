from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .functions import flight_details_filler, initial_fill_attributes
from .model_choices_dictionaries import cities_and_codes


class FlightDetails(models.Model):
    objects = models.Manager()
    CITIES_CHOICES = [(str(city), str(city)) for city in sorted(list(cities_and_codes.keys()))]
    ADULTS_CHOICES = [(i, i) for i in range(1,10)]
    STOPOVER_CHOICES = [(str(i), str(i)) for i in range(1,49)]

    title = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    fly_from = models.CharField(max_length=30, choices=CITIES_CHOICES)
    fly_to = models.CharField(max_length=30, choices=CITIES_CHOICES)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    min_nights = models.IntegerField(null=True)
    max_nights = models.IntegerField(null=True)
    max_sector_stopovers = models.IntegerField(null=True)
    adults = models.IntegerField(choices=ADULTS_CHOICES, null=True)
    stopover_from = models.CharField(max_length=30, choices=STOPOVER_CHOICES, null=True)
    stopover_to = models.CharField(max_length=30, choices=STOPOVER_CHOICES, null=True)

    iata_city_from = models.CharField(max_length=3, blank=True)
    iata_city_to = models.CharField(max_length=3, blank=True)

    price = models.IntegerField(blank=True, null=True)
    iata_port_from = models.CharField(max_length=3, blank=True, null=True)
    iata_port_to = models.CharField(max_length=3, blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    tequila_affiliate_link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flight-detail', kwargs = {'pk': self.pk})


@receiver(pre_save, sender=FlightDetails)
def pre_save_flight_details_update_handler(sender, instance, **kwargs):
    initial_fill_attributes(instance)
    flight_details_filler(instance)


