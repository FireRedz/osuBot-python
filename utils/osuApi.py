import requests as r
from conf import config
from utils.storage import storage

apikey = config.apiKey
baseURL = f'https://osu.ppy.sh/api/get_beatmaps?k={apikey}&b=[shit]'

def getBeatmap(mapID):
    return baseURL.replace('[shit]', mapID)

