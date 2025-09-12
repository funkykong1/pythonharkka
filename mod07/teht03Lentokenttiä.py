import time
print("Minulla on lista jossa on lentokenttiä sekä niiden ICAO tunnisteet.\nVastaa minulle puhekielellä siitä mitä haluaisit tehdä!! Vaihtoehtoina on :\n Tietokannasta etsiminen \n Tietokantaan lisääminen \n Ohjelmasta poistuminen \n ")
lenkent = {"EFHK" : "Helsinki-Vantaa Airport",
           "EGLL" : "London Heathrow Airport",
           "LIRF" : "Rome Fiumicino Airport",
           "EDDF" : "Frankfurt Airport"

            }

uusi = True


# mullistava teknologia jonka avulla voidaan kommunikoida tietokoneen kanssa ilman että käytetään ykkösiä ja nollia!!
answers = {
            "exit" : -1,
            "poistu" : -1,
            "häivy" : -1,
            "x" : -1,
            "stop": -1,
            "cancel" : -1,
            "poistua" : -1,
            "back" : -1,

            "search" : 0,
            "etsi" : 0,
            "hae" : 0,
            "lookup" : 0,
            "google" : 0,
            "etsiä" : 0,
            "hakemisto" : 0,
            "haku" : 0,

            "lisää" : 1,
            "lisätä" : 1,
            "add" : 1,
            "uusi" : 1,
            "new" : 1
        }

# Etsitään annetusta vastauksesta jokin vastaava sana
def tulkitse_vastaus(va):
    lp = None

    for sana in answers:
        if sana in va:
            lp = answers[sana]
            break

    return lp

while True:

    #aivan suunnattoman hieno algoritmi..
    vast = tulkitse_vastaus(input("Haluatko etsiä tai lisätä tietokantaan jotain? ").lower().strip())

    if vast == -1:
        print("Hyvästi!")
        break
    elif vast == 0:

        # uusi while looppi jotta ei tarvitse aloittaa ohjelmaa uudelleen joka kerta
        while True:
            # Tulostetaan kaikki lentokentät koodeittan
            print(f"Lentokentät tietokannassa ovat {list(lenkent.keys())}")
            icao = input("Valitse lentokenttä ICAO-koodin mukaan. Tyhjä vastaus lopettaa.").upper().strip()

            if icao == "":
                break
            else:
                try:
                    lenkent[icao]
                except KeyError:
                    print("Tunnus ei vastaa mitään tunnettua lentokenttää.")
                    time.sleep(1.5)
                else:
                    print(f"{icao} vastaa kohdetta {lenkent[icao]} !!")
                    time.sleep(1.5)

    elif vast == 1:
        while True:
            print(f"Lentokentät tietokannassa ovat {list(lenkent.keys())}")

            lk = input("Anna uuden lentokentän nimi. Tyhjä vastaus lopettaa.").title().strip()
            if lk == "":
                break
            ic = input("Anna uuden lentokentän ICAO-tunnus. Tyhjä vastaus lopettaa.").upper().strip()
            if ic == "":
                break

            lenkent[ic] = lk
            print(f"Tietokantaan lisätty '{lk}' tunnuksella '{ic}'!!")
            time.sleep(1.5)

        # mikäli vastausta ei ymmärretä, yritä uudelleen!
    else:
        print("Anna vastaukseksi vaan sana jota haluat tehdä, etsiä, lisätä, poistua")
        continue










