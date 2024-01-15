import os
from dotenv import load_dotenv
import json
from connection import connection
from getPlaylists import getPlaylist
from readJson import *

data = getPlaylist(os.getenv("SPOTIFY_TEST2"))

jsonFile = createJson(data)

playlistUsers = getPlaylistUsers(jsonFile)

new_json = set_tracksInJSON(playlistUsers, jsonFile)
new_json = organizeJSON(new_json)

createJSON = json.dumps(new_json)

with open("json/output.json", "w", encoding="UTF-8") as fp:
    fp.write(createJSON)
