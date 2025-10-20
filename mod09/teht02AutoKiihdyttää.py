class Auto:
    def __init__(self,  rekkari, huippu):
        self.rekkari = rekkari
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0
        # yleisesti ottaen en haluaisi laittaa tänne printtiä mutta kaipa se skaalaa tai jotain
        print(f"Auton rekisterikilpi on {self.rekkari}, nopeus on {self.nopeus}, "
              f"huippunopeus on {self.huippu}km/h ja kuljettu matka {self.matka}km!!")

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        # kato että onko liian korkea tai matala
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        elif self.nopeus < 0:
            self.nopeus = 0



auto = Auto("ABC-123", 142)
print(f"Luotu auto rekkarilla {auto.rekkari} ja huippunopeudella {auto.huippu}km/h")
print(f"Auton {auto.rekkari} nopeus on {auto.nopeus}!")
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Kiihdytyksen jälkeen auton {auto.rekkari} nopeus on {auto.nopeus}km/h!!!")
auto.kiihdytä(-200)
print(f"Hätäjarrutus !! auton {auto.rekkari} nopeus on nyt {auto.nopeus}km/h")