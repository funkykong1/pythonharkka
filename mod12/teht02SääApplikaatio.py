import requests
import json

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.chucknorris.io/jokes/random"


try:
    vastaus = requests.get(pyyntö)
    val = vastaus
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus["value"], indent=2))
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu toteuttaa en keksinyt mitään")

