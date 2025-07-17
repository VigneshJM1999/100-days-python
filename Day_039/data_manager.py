import requests
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ["SHEETY_ENDPOINT"]
AUTH_HEADER = {
    "Authorization": os.environ["Authorization"]
}

class DataManager:

    def __init__(self):
        self.endpoint = ENDPOINT
        self.headers = AUTH_HEADER
        self.response = requests.get(url=self.endpoint, headers=self.headers)

    def get_data(self):
        return self.response.json()["prices"]

    def update_data(self, data):
        update_url = f"{self.endpoint}/{data['id']}"
        new_data = {
            "price": {
                "iataCode": data["iataCode"]
            }
        }
        self.response = requests.put(url=update_url, json=new_data, headers=self.headers)
