import random
from time import sleep
class Kilpailu:
    def __init__(self, autot, nimi = "romuralli grande", pituus = 10000):
        self.autot = autot
        self.nimi = nimi
        self.pituus = pituus
        self.tunnit = 0

    def kilpailu_ohi(self):
        for car in self.autot:
            if car.matka >= self.pituus:
                return True
        return False

    def tulosta_tilanne(self):
        place = 0
        # pähee taulukko
        print(f"------------------------------------ {self.nimi} ------------------------------------")
        for automobile in self.autot:
            place += 1
            print(f"{place}. Sijalla {automobile.rekkari}, joka on kulkenut {automobile.matka} kilometriä !! -- huippunopeus {automobile.huippu}km/h --")
        print(f"-------------------------------------- Tunti {self.tunnit} ------------------------------------------\n")

    def tunti_kuluu(self, tuntimäärä = 1):
        # toista tuntimäärä kertaa
        for j in range(0, tuntimäärä):
            self.tunnit += 1
            for automobile in self.autot:
                # auto joko hidastaa tai kiihdyttää
                automobile.kiihdytä(random.randint(-10, 16))
                # se kulkee 1h näin
                automobile.kulje(1)

            # järjestä kisan sijoituksen mukaan
            def sorter(kar):
                return kar.matka
            self.autot.sort(key=sorter, reverse=True)

            #kova
            if self.tunnit % 10 == 0:
                # alkutekstiö ei sitten millään nähdä ilman tätä
                sleep(1)
                self.tulosta_tilanne()

            if self.kilpailu_ohi():
                print(f"Auto {self.autot[0].rekkari} voitti kisan kuljettuaan {self.autot[0].matka}km!!!\n"
                f"Aikaa meni {self.tunnit} tuntia\n")
                self.tulosta_tilanne()

class Auto:
    def __init__(self, rekkari, huippu):
        self.rekkari = rekkari
        self.nopeus = 0
        self.huippu = huippu
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # kato että onko liian korkea tai matala
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.matka += tunnit * self.nopeus

# autolista jota ei käytetä enää tän jälkeen btw koska tehtävänannossa oli että kisalla pitää olla PARAMETRINA autojen lista >:(
kaarat = list()
# I <3 max exclusive ranges
for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    kaarat.append(auto)

kisa = Kilpailu(kaarat, "Suuri Romuralli", 8000)


def race():
    print(f"Kisa on käynnissä {len(kisa.autot)} autolla!!!!")
    while not kisa.kilpailu_ohi():
        kisa.tunti_kuluu(1)


race()


