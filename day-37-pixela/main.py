import os
from datetime import datetime

import requests

USERNAME = "erik-pixela"
TOKEN = os.environ['pixelaToken']
print(TOKEN)

pixela_endpoint = "https://pixe.la/v1/users"
user_endpoint = "https://pixe.la/@erik-pixela"
graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph1_endpoint = f"{graphs_endpoint}/graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

# create user
user_params = {
    # "token": os.environ['pixela'],
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create graph
graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

today = datetime.now()
print(today)
# create pixel entry
graph1_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.2",
}

pin_graph = {
    "pinnedGraphID": "graph1"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# "Success. Let's visit https://pixe.la/@erik-pixela , it is your profile page!"
#
# response = requests.post(url=graphs_endpoint, json=graph_config, headers=headers)
# print("response is: " + response.text)

# response = requests.post(url=graph1_endpoint, json=graph1_config, headers=headers)

# set pinned graph
response = requests.put(url=user_endpoint, json=pin_graph, headers=headers)
print(response)
