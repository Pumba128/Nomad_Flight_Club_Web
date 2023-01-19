from .models import FlightDetails
from celery import shared_task
import requests
from django.core.mail import send_mail
from nomad_flight_club.settings import EMAIL_HOST_USER
from .functions import flight_details_filler


@shared_task()
def flight_details_update_celery():
    flights_objects = FlightDetails.objects.all()
    for flight_details in flights_objects:
        old_price = flight_details.price
        if flight_details_filler(flight_details):
            if old_price > flight_details.price:
                flight_details.save()
                send_email_new_flight_connection(flight_details)
        else:
            continue

    return 'Update done'


def send_email_new_flight_connection(flight_details):
    user = flight_details.user
    email_subject = 'New cheapest flight on the radar!'
    email_body = f'Heyo {user.username}! A new flight from {flight_details.title} has been found. New lowest price is' \
                 f' {flight_details.price}€. Go check you flights list!'
    send_mail(subject = email_subject, message = email_body, from_email = EMAIL_HOST_USER, recipient_list = [user.email],
              fail_silently = True)
