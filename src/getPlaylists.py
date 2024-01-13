from connection import *
import os
import json
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from dotenv import load_dotenv
import asyncio

def getPlaylist(spotify_id):
    d = []
    totalNexts = 0
    sp = connection()
    
    results = sp.playlist_items(spotify_id,limit=100)

    if results["next"] is None:
        d.append(results)
        new_data = createJson(d, 0)
        return new_data


    while results["next"] is not None:
        d.append(results)
        
        results = sp.next(results)
        totalNexts += 1 

        if type(results["next"]) == type(None):
            totalNexts += 1
            d.append(results)
            data = createJson(d, totalNexts)            
            return data
   
def createJson(result, nexts):
    json_D = json.dumps(result)
    data = json.loads(json_D)
    data = removeFields(data, nexts)

    return data


def removeFields(playlist, nexts):

    new_data = []

    if nexts == 0:
        for item in playlist[0]["items"]:
            new_item = {
            "added_by": item["added_by"]["id"],
            "track_id": item["track"]["id"],
            "track_name": item["track"]["name"],          
            }
            new_data.append(new_item)
        new_data = json.dumps(new_data)

        return new_data

    for next in range(nexts):
        for item in playlist[next]["items"]:
            new_item = {
            "added_by": item["added_by"]["id"],
            "track_id": item["track"]["id"],
            "track_name": item["track"]["name"],          
            }
            new_data.append(new_item)
    new_data = json.dumps(new_data)
    return new_data

