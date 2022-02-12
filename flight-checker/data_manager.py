# Data Manager Class
# This class is responsible for talking to the Google Sheet.

import requests
import os

TOKEN = {
    "Authorization": f"Bearer {os.getenv('AUTHORIZATION')}"
}
SHEETY_ENDPOINT = "https://api.sheety.co/d91dde19987ca0e425b0a3014474ccc7/flightDeals/prices"

class DataManager:

    def __init__(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=TOKEN)
        self.prices = response.json()["prices"]

    def edit_sheet_code(self, code, sheet_id):
        edit_code = {
            "price": {
                "iataCode": code
            }
        }
        sheety_update_endpoint = f"{SHEETY_ENDPOINT}/{sheet_id}"
        requests.put(url=sheety_update_endpoint, json=edit_code, headers=TOKEN)

    def edit_sheet_price(self, price, sheet_id):
        edit_code = {
            "price": {
                "lowestPrice": price
            }
        }
        sheety_update_endpoint = f"{SHEETY_ENDPOINT}/{sheet_id}"
        requests.put(url=sheety_update_endpoint, json=edit_code, headers=TOKEN)
