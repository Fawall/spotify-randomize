import os
from dotenv import load_dotenv
import json
from connection import connection
from getPlaylists import getPlaylist
from readJson import *

data = getPlaylist(os.getenv("SPOTIFY_TEST3"))

with open("json/tracks.json", "w", encoding="utf-8") as fp:
    fp.write(data)

jsonFile = "json/tracks.json"
file = readJson(jsonFile)

playlistUsers = getPlaylistUsers(file)

new_json = set_tracksInJSON(playlistUsers, file)

new_json = organizeJSON(new_json)

createJSON = json.dumps(new_json)

with open("json/output.json", "w", encoding="UTF-8") as fp:
    fp.write(createJSON)





