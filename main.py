import telegram
import requests

from spotipy.oauth2 import SpotifyOAuth

def get_spotify_token():
    # Get the Spotify token.
    client_id = "YOUR_CLIENT_ID_HERE"
    client_secret = "YOUR_CLIENT_SECRET_HERE"
    redirect_uri = "YOUR_REDIRECT_URI_HERE"
    scope = "user-library-read,playlist-modify-public"
    token = SpotifyOAuth(client_id, client_secret, redirect_uri, scope)
    token.get_access_token()
    return token

def play_song(song_name):
    # Play the song on Spotify.
    token = get_spotify_token()
    sp = spotipy.Spotify(auth=token)
    song = sp.search(q=song_name, type="track")
    song_uri = song["tracks"]["items"][0]["uri"]
    sp.start_playback(uris=[song_uri])

def music_handler(update, context):
    chat_id = update.effective_chat.id
    song_name = update.message.text
    play_song(song_name)

app = telegram.Bot(token="YOUR_TOKEN_HERE")
app.add_handler(telegram.CommandHandler("play", music_handler))

app.polling()
