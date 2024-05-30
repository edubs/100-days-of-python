import requests
import os

LAT = 43.064911
LON = -70.767090
# need to set environment variable
API_KEY = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
