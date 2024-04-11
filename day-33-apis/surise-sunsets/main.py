import requests
from datetime import *

MY_LAT = 43.064911
MY_LONG = -70.767090

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # hour position only
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]  # hour position only

print(sunrise)

time_now = datetime.now()

print(time_now.hour)
