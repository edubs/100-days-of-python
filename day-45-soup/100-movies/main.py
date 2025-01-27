import requests
from bs4 import BeautifulSoup

# response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
# empire_page = response.text
with open("movies.htm") as file:
    empire_page = file.read()

soup = BeautifulSoup(empire_page, "html.parser")
movies = soup.find_all("h3")
# get text from h3 element, replace new line char with space, split string to remove extra white space
# then finally join the elements with a single space character
movie_list = [' '.join(movie.getText().replace("\n", " ").split()) for movie in movies]
rev_movie_list = movie_list[::-1]

# print the list in reverse order (start with 1 and work to 100) one element at a time
for each in rev_movie_list:
    print(each)

with open("movies.txt", mode="w") as file:
    for movie in rev_movie_list:
        file.write(f"{movie}\n")
