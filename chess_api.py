# boilerplate ideas
# I want to take the work out of the javascript on my site and only have it query this API

import requests
import json
from time import sleep


def getJson():
    url = 'https://api.chess.com/pub/player/ajze/games'
    r = requests.get(url)
    res = json.loads(r.content)

    for item in res['games']:
        if item['black'].find('anebir') != -1 or item['white'].find('anebir') != -1:

        # do the things


def processData():


def saveData():


def sendToAPI():


def start():
    while True:
        getJson()
        sleep(60)  # 15 minutes = 900


if __name__ == '__main__':
    start()


