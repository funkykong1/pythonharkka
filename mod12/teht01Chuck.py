import requests


def weather():
    while True:
        nimi = input("Give me the name of a city and I will tell u the weather data of said city\n"
                     "name of city ---->>> ")

        # katotaan saadaanko kaupungin nimen perusteella löydettyä mitään
        # ei tarvita mitää latitude longitudea tähän
        try:
            pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={nimi}&appid=181b2c2835ff3e9c701b341d5776beb3&units=metric"
            vastaus = requests.get(pyyntö).json()

            # laitetaan metric sinne pyyntöön niin ei tarvii muuttaa kelvineitä mihkään muuhun
            temp_real = round(vastaus["main"]["temp"])
            temp_feels = round(vastaus ["main"]["feels_like"])

            print(f"\n------------------------------------------------------------\n"
                  f"Weather of {nimi}, {vastaus["sys"]["country"]} is {vastaus["weather"][0]["description"]}\n"
                  f"The temperature is {temp_real} °C and it feels like {temp_feels} °C\n"
                  f"The wind speed is {vastaus ["wind"]["speed"]} m/s !!\n"
                  f"------------------------------------------------------------")
        except requests.exceptions.RequestException as e:
            print("Cudnt find a thing with ur input cuz of the following :" )
            print(e)
        except KeyError:
            print(f"Didnt find a city with the name {nimi}\n")


weather()