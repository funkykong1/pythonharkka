class Auto:
    def __init__(self,  rekkari, huippu):
        self.rekkari = rekkari
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0
        # yleisesti ottaen en haluaisi laittaa tänne printtiä mutta kaipa se skaalaa tai jotain
        print(f"Auton rekisterikilpi on {self.rekkari}, nopeus on {self.nopeus}, "
              f"huippunopeus on {self.huippu}km/h ja kuljettu matka {self.matka}km!!")


auto = Auto("ABC-123", 142)
