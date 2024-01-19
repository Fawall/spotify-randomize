import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from connections import connection
from dotenv import load_dotenv
from connections import create_playlist_connection
import os

load_dotenv()


def create_playlist(playlist_name):
    
    username = os.getenv("USER_SPOTIFY")
    sp = create_playlist_connection()

    sp.user_playlist_create(user=username,name=playlist_name,collaborative=False)

