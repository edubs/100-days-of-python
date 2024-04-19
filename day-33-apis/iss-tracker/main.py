import requests
from datetime import *

MY_LAT = 43.064911
MY_LONG = -70.767090


# Get sunrise / sunset times
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # hour position only
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # hour position only

    # Get current time
    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


# calculate relative position of ISS
def is_iss_overhead():
    # Get ISS position
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    print(f"ISS Lat: {iss_lat}")
    print(f"ISS Long: {iss_long}")
    print(f"My Lat: {MY_LAT}")
    print(f"My Long: {MY_LONG}")

    abs_long = round(abs(MY_LONG - iss_long))
    abs_lat = round(abs(MY_LAT - iss_lat))

    if abs_lat < 5 and abs_long < 5:
        return True


if is_iss_overhead() and is_night():
    # send email
    print("It's night and the ISS is nearby.")
else:
    print("It's day or the ISS is not nearby.")
