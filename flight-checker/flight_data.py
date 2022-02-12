# Flight Data Class
#This class is responsible for structuring the flight data.

class FlightData:

    def __init__(self, city_from, ap_from, city_to, ap_to, arrival_date, departure_date, airlines, price):
        self.city_from = city_from
        self.airport_from = ap_from
        self.city_to = city_to
        self.airport_to = ap_to
        self.destination_arrival = arrival_date
        self.destination_departure = departure_date
        self.airlines = airlines
        self.price = price
