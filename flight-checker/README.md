# Flight Checker

## Program
1. This program reads through a google sheet containing a city name, IATA code, and price of the cheapest flight.
- It is read using an API from Sheety.
2. After it finds the city name and IATA code, using the Tequila.kiwi API to find flights from Las Vegas to any location will return a JSON file of flights cheapest to more expensive.
3. If the cheapest flight is cheaper than the flight on the google sheet, then the program will send a message to my phone using a Twilio API.
