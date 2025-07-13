import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")

MY_LATITUDE = 13.082680
MY_LONGITUDE = 80.270721
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

parameters = {
    "lat":MY_LATITUDE,
    "lon":MY_LONGITUDE,
    "appid":API_KEY,
    "cnt":4,
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
raw_data = response.json()["list"]
weather_data = [weather["weather"][0]["id"] for weather in raw_data]

for weather in weather_data:
    if weather < 700:
        print()
        message = client.messages.create(
            from_="whatsapp:+10123456789",
            body="It is going to rain today ⛈️. So, bring umbrella ☔.",
            to="whatsapp:+910123456789",
        )
        break
