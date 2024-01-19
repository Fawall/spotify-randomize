import os
import json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from spotipy import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()


def connection():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                            client_secret=client_secret))
    return sp


def create_playlist_connection():

    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-public",
            
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            redirect_uri="https://google.com"    
        )
    )
    return sp


