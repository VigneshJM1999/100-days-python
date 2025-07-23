import requests
from bs4 import BeautifulSoup
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv()
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
DISPLAY_NAME = os.environ["DISPLAY_NAME"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=DISPLAY_NAME,
    )
)

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=header)

billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")

title_tags = soup.select("li ul li h3")
titles = [title.get_text().strip() for title in title_tags]

year = date.split("-")[0]

title_uris = []

for title in titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        title_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description=f"Top 100 songs from Billboard on {date}"
)

sp.playlist_add_items(playlist_id=playlist["id"], items=title_uris)
print(f"Successfully created playlist: {playlist['name']}")
