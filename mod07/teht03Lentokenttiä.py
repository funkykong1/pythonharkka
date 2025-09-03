import time
print("Minulla on lista jossa tulisi olla lentokenttiä sekä niiden ICAO tunnisteet.\n Voit etsiä tietokannasta tai lisätä siihen uuden artikkelin.")
lenkent = {"EFHK" : "Helsinki-Vantaa Airport",
           "EGLL" : "London Heathrow Airport",
           "LIRF" : "Rome Fiumicino Airport",
           "EDDF" : "Frankfurt Airport"

            }

uusi = True


# mullistava teknologia jonka avulla voidaan kommunikoida tietokoneen kanssa ilman että käytetään ykkösiä ja nollia!!
answers = {"en" : False,
           "ei" : False,
           "0" : False,
           "ei kiitos" : False,
           "no" : False,
           "false" : False,

           "joo" : True,
           "juu" : True,
           "kyllä" : True,
           "yep" : True,
           "yes" : True,
           "kyllä kiitos" : True,
           "true" : True,
           "1" : True

        }
def tulkitse_vastaus(vast):
    lp = None

    for v in answers:
        if vast == v:
            lp = answers[v]

    return lp

while True:
    lippu = None

    if uusi:
        t = input("Haluatko etsiä tietokannasta jotain? ").lower()

        lippu = tulkitse_vastaus(t)

        # Mikäli vastausta ei ymmärretä, yritä uudelleen
        if lippu is None:
            print("En ymmärtänyt vastaustasi, voisitko puhua selvemmin :-) iha vaan joo tai ei riittää")
            continue

        uusi = False


    while lippu == True:

        print(f"Lentokentät tietokannassa ovat {list(lenkent.keys())}")

        icao = input("Etsi lentokenttää ICAO-koodin mukaan. Tyhjä vastaus lopettaa.").upper().strip()

        if icao == "":
            break
        else:

            try:
                lenkent[icao]
            except KeyError:
                print("Tunnus ei vastaa mitään tunnettua lentokenttää.")
            else:
                print(f"{icao} vastaa kohdetta {lenkent[icao]} !!")

            # on vähän kivempi kun haettu tieto ilmestyy ja siihen ei heti tule samaa hakemistoa peräjälkeen
            time.sleep(1)


    while lippu == False:
        lk = input("Anna uuden lentokentän nimi. Tyhjä vastaus lopettaa.").title().strip()
        if lk == "":
            break
        ic = input("Anna uuden lentokentän ICAO-tunnus. Tyhjä vastaus lopettaa.").upper().strip()
        if ic == "":
            break

        lenkent[ic] = lk
        print(f"Tietokantaan lisätty {lk} tunnuksella {ic}!!")

    uusi = True











