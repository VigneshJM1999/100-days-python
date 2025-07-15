import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "calory",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print("Graph creation:", response.text)

today = datetime.now()
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1000"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Pixel creation:", response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "1100"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print("Pixel update:", response.text)

delete_endpoint = update_endpoint

response = requests.delete(url=delete_endpoint, headers=headers)
print("Pixel deletion:", response.text)
