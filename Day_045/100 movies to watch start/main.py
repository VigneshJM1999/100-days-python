import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)

bm_website = response.text

soup = BeautifulSoup(bm_website, "html.parser")
title_tag = soup.find_all("h3", class_="title")
titles = [title.get_text().encode('latin1').decode('utf-8') for title in title_tag]
titles.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in titles:
        file.write(f"{movie}\n")
