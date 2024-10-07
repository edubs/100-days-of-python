import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_page = response.text

soup = BeautifulSoup(empire_page, "html.parser")
movies = soup.find_all("h3")
for movie in movies:
    print(movie.getText())
