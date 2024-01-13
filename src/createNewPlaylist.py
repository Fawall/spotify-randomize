import spotipy
from spotipy.oauth2 import SpotifyOAuth
from connection import connection


def createPlaylist(user, playlist_name,public):
    sp = connection()

    ok = sp.user_playlist_create(user,playlist_name,public,False)

    return ok
    