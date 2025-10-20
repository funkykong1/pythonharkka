import random

kaarat = list()


# printit sikseen koska en halua viittäkymmentä riviä
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


# I <3 max exclusive ranges
for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    kaarat.append(auto)

def race():
    print(f"Kisa on käynnissä {len(kaarat)} autolla!!!!")
    h = 0
    while True:
        for kaara in kaarat:
            # auto joko hidastaa tai kiihdyttää
            kaara.kiihdytä(random.randint(-10, 16))
            # se kulkee 1h näin
            kaara.kulje(1)
            h += 1
            if kaara.matka >= 10000:
                print(f"\nAuto {kaara.rekkari} voitti kisan kuljettuaan {kaara.matka}km!!!\n"
                      f"Aikaa meni {h} tuntia\n")
                return


# aivan hävyttömän outo funktio
def sorter(kar):
    return kar.matka

race()
# järjestä kisan sijoituksen mukaan
kaarat.sort(key=sorter, reverse=True)


i = 0
for car in kaarat:
    i += 1
    print(f"{i}. Sijalla {car.rekkari}, joka kulki {car.matka} kilometriä huippunopeudellaan {car.huippu}km/h!")
