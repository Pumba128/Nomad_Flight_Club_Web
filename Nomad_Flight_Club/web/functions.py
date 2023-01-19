import requests
from django.utils.text import slugify
import os

API_KEY = os.environ.get('TEQUILA_API_KEY')
END_SEARCH = "https://api.tequila.kiwi.com/v2/search?"


def request_parameters_create(flight_details):
    request_parameters = {
            'fly_from': f'city:{flight_details.iata_city_from}',
            'fly_to': f'city:{flight_details.iata_city_to}',
            'date_from': flight_details.from_date,
            'date_to': flight_details.to_date,
            'nights_in_dst_from': flight_details.min_nights,
            'nights_in_dst_to': flight_details.max_nights,
            'limit': 1,
            'max_sector_stopovers': flight_details.max_sector_stopovers,
            'stopover_from': '{}:00'.format(flight_details.stopover_from),
            'stopover_to': '{}:00'.format(flight_details.stopover_to),
            'adults': flight_details.adults,
        }
    return request_parameters


def tequila_search_request_call(flight_details):
    request_parameters = request_parameters_create(flight_details)
    request_headers = {
        'Accept-Encoding': 'gzip' ,
        'Content-Type': 'application/json' ,
        'apikey': API_KEY
    }
    call_response = requests.get(url = END_SEARCH , headers = request_headers , params = request_parameters)
    try:
        search_data = call_response.json()['data'][0]
        return search_data
    except IndexError:
        return None
    except KeyError:
        return None


def flight_details_filler(flight_details):
    new_flight_data = tequila_search_request_call(flight_details)
    if new_flight_data:
        flight_details.price = new_flight_data['price']
        flight_details.iata_port_from = new_flight_data['flyFrom']
        flight_details.iata_port_to = new_flight_data['flyTo']
        flight_details.nights = new_flight_data['nightsInDest']
        flight_details.departure_date = new_flight_data['route'][0]['local_departure'].split("T")[0]
        flight_details.arrival_date = new_flight_data['route'][-1]['local_arrival'].split("T")[0]
        flight_details.tequila_affiliate_link = new_flight_data['deep_link']
        return flight_details
    else:
        return None


def initial_fill_attributes(instance):
    instance.title = '{} to {}'.format(instance.fly_from , instance.fly_to)
    instance.slug = slugify(instance.title)
    instance.iata_city_from = instance.cities_and_codes[instance.fly_from]
    instance.iata_city_to = instance.cities_and_codes[instance.fly_to]