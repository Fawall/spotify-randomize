import os
from dotenv import load_dotenv
import json
from connections import connection
from getPlaylists import getPlaylist
from createPlaylist import *
from readJson import *

data = getPlaylist(os.getenv("SPOTIFY_TEST2"))

jsonFile = createJson(data)

playlistUsers = getPlaylistUsers(jsonFile)

new_json = set_tracksInJSON(playlistUsers, jsonFile)
new_json = organizeJSON(new_json)

createJSON = json.dumps(new_json)

create_playlist("newPlaylist")

if not os.path.exists("json"):
    os.makedirs("json")

with open("json/output.json", "w", encoding="UTF-8") as fp:
    fp.write(createJSON)
