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

class SähköAuto(Auto):
    def __init__(self, rekkari, huippu, akku):
        super().__init__(rekkari,huippu)
        self.tankki = akku

class MoottoriAuto(Auto):
    def __init__(self, rekkari, huippu, tankki):
        super().__init__(rekkari,huippu)
        self.tankki = tankki




# en varmaan tee siitä mitään stringiä johon kuuluu joku litrayksikkö
tesler = SähköAuto("ABC-15", 180, [52.5, "kWh"])
bemw = MoottoriAuto("ACD-123", 165, [32.5, "l"])

for car in [tesler, bemw]:
    car.kiihdytä(300)
    car.kulje(3)
    print(f"kaara {car.rekkari} liikkeessä vauhdilla {car.nopeus} km/h, matkaa kuljettu {car.matka} km.\n"
          f"Autossa mehua {str(car.tankki[0]) + " " + car.tankki[1]}")

