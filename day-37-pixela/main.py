import os
import requests

USERNAME = "erik-pixela"
TOKEN = "nSpYswn6n3hktHO2kvaFwFXi"

pixela_endpoint = "https://pixe.la/v1/users"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph1_endpoint = f"{graphs_endpoint}/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    # "token": os.environ['pixela'],
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

graph1_config = {
    "date": "20240616",
    "quantity": "4.15",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# "Success. Let's visit https://pixe.la/@erik-pixela , it is your profile page!"
#
# response = requests.post(url=graphs_endpoint, json=graph_config, headers=headers)
# print("response is: " + response.text)

response = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)
