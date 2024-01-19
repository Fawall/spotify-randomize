import os
from dotenv import load_dotenv
import json
from connections import connection
from getPlaylists import getPlaylist
from CreateNewPlaylist import *
from readJson import *

data = getPlaylist(os.getenv("SPOTIFY_TESTE"))

jsonFile = createJson(data)

playlistUsers = getPlaylistUsers(jsonFile)

new_json = set_tracksInJSON(playlistUsers, jsonFile)
json_with_tracks = organizeJSON(new_json)

createJSON = json.dumps(json_with_tracks)

id_playlist = create_playlist("new playlist")

populate_playlist(id_playlist,json_with_tracks)

if not os.path.exists("json"):
    os.makedirs("json")

with open("json/output.json", "w", encoding="UTF-8") as fp:
    fp.write(createJSON)
