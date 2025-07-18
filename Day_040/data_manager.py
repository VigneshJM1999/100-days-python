import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.sheety_username = os.environ["SHEETY_USERNAME"]
        self.sheety_password = os.environ["SHEETY_PASSWORD"]
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]
        self.headers = {
            "Authorization": f"Basic {os.environ['SHEETY_BASIC_AUTH']}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.prices_endpoint, headers=self.headers)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers
            )

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers=self.headers)
        users_data = response.json()["users"]
        return users_data