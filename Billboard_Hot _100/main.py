from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

CLIENT_ID = "9adc7a2e9f3a47248b45e9521b710691"
CLIENT_SECRET = "7bd6d68df2424ec2af38b732518ed5a3"
REDIRECT_URI = "http://example.com"

input_year = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{input_year}")
website_source= response.text
soup = BeautifulSoup(website_source, "html.parser")
song_title = soup.find_all(name="span", class_="chart-element__information__song")
song_list = [song.getText() for song in song_title]



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               ))
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = input_year.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song}, year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{input_year}Billboard 100", public=False)
print(playlist)



# # print(website_source)
#
#
# print(song_list)