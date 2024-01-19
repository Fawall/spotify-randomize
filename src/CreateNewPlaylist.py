import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from connections import connection
from dotenv import load_dotenv
from connections import create_playlist_connection
import os

load_dotenv()

def create_playlist(playlist_name):

    sp = create_playlist_connection()
    username = os.getenv("USER_SPOTIFY")
    create = sp.user_playlist_create(user=username,name=playlist_name,collaborative=False)
    playlist_id = create["id"]

    return playlist_id
    

def populate_playlist(id_playlist,tracklist):
    sp = create_playlist_connection()
    for track in tracklist:
        sp.user_playlist_add_tracks(user=os.getenv("USER_SPOTIFY"),playlist_id=id_playlist,tracks=[track],position=None)