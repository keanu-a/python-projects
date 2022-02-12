# Notification Manager Class
# This class is responsible for sending notifications with the deal flight details.

from twilio.rest import Client
import os

class NotificationManager:

    def __init__(self, flight):
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")

        client = Client(account_sid, auth_token)
        client.messages.create(
            body=f"Low Price Alert! Only ${flight.price} to fly from {flight.city_from}-{flight.airport_from} to "
                 f"{flight.city_to}-{flight.airport_to}, "
                 f"from {flight.destination_arrival} to {flight.destination_departure}.",
            from_="+18174063012",
            to="+17025215496",
        )
