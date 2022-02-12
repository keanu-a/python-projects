# Keanu Aloua
# January 4, 2022
# Cheap Flight Alert Program using OOP, APIs, datetime, List and Dictionary Comprehensions

# This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

sheet_data = DataManager()

# Goes through each row in the sheet
for d in sheet_data.prices:
    sheet_city = d["city"]
    sheet_id = d["id"]

    try:
        sheet_price = d["lowestPrice"]
    except KeyError:
        sheet_price = 0

    city = FlightSearch(f"{sheet_city}")  # Returns IATA Code for the city

    # If there is no iata code in the sheet then it will input
    if d["iataCode"] == "":
        sheet_data.edit_sheet_code(city.found_code, sheet_id)
        print(f"{sheet_city} IATA code was updated")

    # Finds the cheapest flight for that city from tomorrow through 6 months from now
    cheapest_flight = city.find_flight()

    # If cheaper flight is found then will send an SMS and update google sheets
    if cheapest_flight.price < sheet_price or sheet_price == 0:
        NotificationManager(cheapest_flight)

        # Changes the Google sheet to show the cheaper price
        sheet_data.edit_sheet_price(cheapest_flight.price, sheet_id)

