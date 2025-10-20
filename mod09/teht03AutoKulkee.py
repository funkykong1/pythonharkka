class Auto:
    def __init__(self,  rekkari, huippu):
        self.rekkari = rekkari
        self.nopeus = 0
        self.huippu = huippu
        self.matka = 0
        print(f"Luotu kaara rekkarilla {rekkari} jonka huippunopeus on {huippu}km/h")

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # kato että onko liian korkea tai matala
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        elif self.nopeus < 0:
            self.nopeus = 0

        print(f"Kiihdytyksen jälkeen auton {auto.rekkari} nopeus on {auto.nopeus}!!!\n")

    def kulje(self, tunnit):
        print(f"Auton {self.rekkari} kuljettu matka on {self.matka} km")

        # lissää kulujettuun matkaan tuntinopeus * tuntien MÄÄRÄ
        self.matka += tunnit * self.nopeus
        print(f"Tämä auto kulki {tunnit}h ajan vauhdilla {self.nopeus} km/h!"
              f"\nUusi kokonaismatka on nyt {self.matka} km\n")



auto = Auto("ABC-123", 142)
auto.kiihdytä(80)

auto.kulje(3)

auto.kulje(12)
