import requests as r
from conf import config
from utils.storage import storage

apikey = config.apiKey
baseURL = f'https://osu.ppy.sh/api/get_beatmaps?k={apikey}&b=[shit]'

def getBeatmap(mapID):
    try:
        tempReq = r.get(baseURL.replace('[shit]', mapID)).json()[0]
    except:
        tempReq = None
    
    return tempReq

