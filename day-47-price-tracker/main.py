import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

practice_url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(practice_url)
instant_pot = response.text
soup = BeautifulSoup(instant_pot, "html.parser")

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Price without currency symbol
just_price = price.split("$")[1]

# convert to float
float_price = float(just_price)
print(float_price)

# ====================== Send an Email ===========================
# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

load_dotenv()

if float_price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
        )
