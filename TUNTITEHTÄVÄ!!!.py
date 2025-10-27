otukset = list()

class Yritys:
    def __init__(self, nimi):
        self.nimi = nimi
        self.hoitolat = list()

    def anna_joululahja(self):
        pass

yritys = Yritys("Musti ja mirri")

class Creature:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        # tää on aika siistiä
        otukset.append(self)

    def hauku(self, kerrat = 1):
        for i in range(kerrat):
            print(self.nimi + " äänelehtii: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self, nimi):
        self.elukat = []
        self.nimi = nimi
        yritys.hoitolat.append(self)

    def lisää_elukka(self, elukka):
        self.elukat.append(elukka)
        print(f"{elukka.nimi} lisätty hoitolan {self.nimi} kirjoihin!!")

    def karkota_elukka(self, elukka):
        self.elukat.remove(elukka)
        print(f"{elukka.nimi} lähetettiin kadotukseen hoitolasta {self.nimi}!!\n"
              f"se oli {2025-elukka.syntymävuosi}v vanha :-)")

    def tervehdi_elukoita(self):
        for e in self.elukat:
            e.hauku(1)


olio1 = Creature("Ressu", 2016)
olio2 = Creature("Lassi", 2021, "hau hau")
olio3 = Creature("Cricket", 2019, "Mau")
olio4 = Creature("Lapsukka", 2012, "Miu mau")
olio4 = Creature("Rontti", 2017, "Miu miu")

hoitola1 = Hoitola("Karvapallojen Kokoomus")
hoitola2 = Hoitola("Creature Feature")






while True:
    p = 1
    # Hoitola numerolista
    arr = list()
    for h in yritys.hoitolat:
        arr.append(p)
        p += 1

    p = 0
    while p not in arr:
        print(f"Hoitoloita on seuraavia:")

        for h in range(1, len(yritys.hoitolat)+1):
            print(f"{h}. {yritys.hoitolat[h - 1].nimi}")

        p = int(input(f"Valitse yksi, johon haluat mennä \n > "))

    h = yritys.hoitolat[p-1]
    hoitolassa = True

    while hoitolassa:
        p = -1
        i = 1
        l = 1
        while p not in range(0, len(h.elukat)+2):
            print(f"Eläimiä hoitolassa {h.nimi} on seuraavia:")
            for e in h.elukat:
                print(f"{l}.{e.nimi}")
                l += 1

            print(f"{l} --> Lisää elukka")
            print(f"0 --> Poistu")

            p = int(input(f"Valitse eläin, jonka haluat karkottaa\n > "))
        # lisää
        if p == l:
            i = 1
            for o in otukset:
                print(f"{i}. {o.nimi}")
                i += 1

            i = int(input(f"Valitse olento numeron mukaan, jonka haluat lisätä btw en siedä vääriä vastauksia \n > "))
            h.lisää_elukka(otukset[i-1])


        elif p == 0:
            hoitolassa = False



        # karkota
        else:
            p -= 1

            h.elukat[p].hauku(1)
            e = ""
            while e not in ["y", "n"]:
                e = input(f"Karkota {h.elukat[p].nimi}? Y/N \n > ").strip().lower()

            if e == "y":
                h.elukat[p].hauku(1)
                h.karkota_elukka(h.elukat[p])
            else:
                h.elukat[p].hauku(1)





