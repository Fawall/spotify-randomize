import json

def createJson(file):
    data = json.loads(file)
    return data


def getPlaylistUsers(file):
       
    users = set()

    for d in file:
        users.add(d["added_by"])

    return users
        
def set_tracksInJSON(user,file):
    convertToUsers = list(user)
    usersPlaylist = {user: [] for user in convertToUsers}

    for track in file:       
        
        if "added_by" in track and track["added_by"] in usersPlaylist:
            usersPlaylist[track["added_by"]].append(track["track_name"])

    return usersPlaylist

def organizeJSON(file):
    j = 0
    i = 0
    tracks = list(file.items())
    first_values = []

    for i in range(len(tracks[0][1])):
         
        for users, sublist in tracks:
            first_values.append(sublist[i]) 

    return first_values

  
    


