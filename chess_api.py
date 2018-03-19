import requests
import json
from time import sleep


def getJson():
    url = 'https://api.chess.com/pub/player/ajze/games'
    r = requests.get(url)

    res = json.loads(r.content)

    for item in res['games']:

        if item['black'].find('anebir') != -1 or item['white'].find('anebir') != -1:

            with open("/var/www/vhosts/jonze.uk/httpdocs/chess.txt", "w") as text_file:
                text_file.write(item['fen'])  # + ','

def start():
    while True:
        getJson()
        sleep(60)  # 15 minutes = 900


if __name__ == '__main__':
    start()


