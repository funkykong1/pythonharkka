import requests
import json

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()

#emt miks tää ei toimi :(
haluttu_vastaus = json.dumps(vastaus[0],indent=2)
print(haluttu_vastaus)
name = vastaus[0]["show"]["name"]
score = vastaus[0]["score"]
genre = vastaus[0]["show"]["genres"][0]

print(f"Ohjelman {name} pistemäärä on {score}. Sen genre on {genre}")