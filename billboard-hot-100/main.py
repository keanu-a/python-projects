# Keanu Aloua
# January 11, 2022
# Web scraping the billboard top 100 to create a spotify playlist

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = "http://example.com"
OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"

URL = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=f"{URL}{date}/")
soup = BeautifulSoup(response.text, "html.parser")

# Gets top 100 songs from Billboard
data = soup.find_all(name="h3", id="title-of-a-story", class_="c-title")
songs = [hit.text for hit in data[5:]]

# Puts top 100 into a list
top_songs = []
for song in songs:
    if songs.index(song) % 4 == 0:
        title = song.split("\n")[1]
        top_songs.append(title)

top_100 = top_songs[:100]  # Lists of billboard top 100

# Spotify Authentication
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token.txt",
    )
)

# Finds user username
user = spotify.current_user()["id"]

# Finds songs URIs
song_uris = []
for song in top_100:
    found_song = spotify.search(q=f"track:{song}", type="track")
    try:
        uri = found_song["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist on Spotify.")

# Creates a playlist
playlist = spotify.user_playlist_create(user=user, name=f"{date} Billboard 100", public="False")
playlist_id = playlist["id"]

# Adds songs to playlist
spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)
