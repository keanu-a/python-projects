# Flight Search Class
# This class is responsible for talking to the Flight Search API.

import requests
from flight_data import FlightData
from datetime import datetime, timedelta
import os

API_KEY = os.getenv("TEQUILA_API_KEY")
TOMORROW = datetime.now().date() + timedelta(days=1)
THROUGH = TOMORROW + timedelta(6 * 30)


class FlightSearch:

    def __init__(self, city):
        headers = {
            "apikey": API_KEY,
        }
        name_params = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=name_params, headers=headers)
        self.found_code = response.json()["locations"][0]["code"]

    def find_flight(self):
        headers = {
            "apikey": API_KEY,
        }
        flight_params = {
            "adults": "1",
            "fly_from": "LAS",
            "fly_to": self.found_code,
            "date_from": TOMORROW.strftime('%d/%m/%Y'),
            "date_to": THROUGH.strftime('%d/%m/%Y'),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "flight_type": "round",
            "max_stopovers": "0",
            "curr": "USD",
        }
        response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=flight_params, headers=headers)
        data = response.json()["data"][0]  # Cheapest Flight

        # Getting data from flight data
        departure_city = data["cityFrom"]
        departure_airport = data["flyFrom"]
        destination_city = data["cityTo"]
        destination_airport = data["flyTo"]
        airlines = data["airlines"][0]
        price = data["price"]
        duration = data["route"]

        # Getting trip duration
        dest_arrival = duration[0]['local_departure'].split(".")[0].split("T")
        dest_arrival = dest_arrival[0]

        dest_departure = duration[1]['local_departure'].split(".")[0].split("T")
        dest_departure = dest_departure[0]

        # Creating a flight object
        cheapest_flight = FlightData(
            departure_city,
            departure_airport,
            destination_city,
            destination_airport,
            dest_arrival,
            dest_departure,
            airlines,
            price
        )

        return cheapest_flight
