# Keanu Aloua
# January 2, 2021
# Creating a rain alert app using API keys and sending SMS

import requests
from twilio.rest import Client
import os

my_key = os.getenv("MY_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
auth_token = os.getenv("AUTH_TOKEN")
account_sid = os.getenv("ACC_SID")

# For Las Vegas
parameters = {
    "lat": 36.050932,
    "lon": -115.191427,
    "appid": my_key,
    "exclude": "current, minutely, daily",
}

response = requests.get(url=weather_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

weather_codes = [item["weather"][0]["id"] for item in data["hourly"][:12]]

for code in weather_codes:
    if code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella! ☂",
        from_=os.getenv("TWILIO_NUM"),
        to="+17025215496",
    )

    print(message.status)
