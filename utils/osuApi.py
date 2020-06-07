import requests as r
from conf import config
from utils.storage import storage

apikey = config.apiKey
baseURL = [f'https://osu.ppy.sh/api/get_beatmaps?k={apikey}&b=[shit]']

def getBeatmap(mapID):
    if mapID in storage.mapData: # check if map exist in storage
        #print('exist!')
        tempReq = storage().getData(mapID)
        return tempReq

    try:
        #print(baseURL[0].replace('[shit]', mapID))
        tempReq = r.get(baseURL[0].replace('[shit]', mapID)).json()[0]
        storage().insertData(mapID, tempReq) # insert map data into storage
    except:
        tempReq = None

    return tempReq

