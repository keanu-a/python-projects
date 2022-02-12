# Keanu Aloua
# January 10, 2022
# Day 45 - Web Scraping a movie website to find top 100 movies

from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
article_movie_headers = soup.find_all(name="h3", class_="title")
movie_titles = [movie.text for movie in article_movie_headers]
# movie_titles.reverse()  # Can use this to reverse list
movies = movie_titles[::-1]  # or splice by [::-1] as seen below to reverse list

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
