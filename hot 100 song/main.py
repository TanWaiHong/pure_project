from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="a9e980bfd9064fe7afa3b6f1e116e9af",
        client_secret="6d106fcd1c1649adad5bb6645b0109eb",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which day do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("h3", id="title-of-a-story")
song_names = [song.getText()[1:-1] for song in song_names_spans if
              song.getText() != '\nSongwriter(s):\n' and song.getText() != '\nProducer(s):\n' and
              song.getText() != '\nImprint/Promotion Label:\n']

song_names = song_names[3:-13]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Top 100 in Billboard", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
