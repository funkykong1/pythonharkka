

class Hissi:
    def __init__(self, alin = 0, ylin = 10):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Menty ylös yksi kerros. Uusi kerros on {self.kerros}")
        # tää ei tee mitään lol
        else:
            print(f"Kerros on jo {self.ylin}, ei voida mennä ylemmäs!!")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Menty alas yksi kerros. Uusi kerros on {self.kerros}")
        else:
            print(f"Kerros on jo {self.alin}, ei voida mennä alemmas!!")

    def siirry_kerrokseen(self, target):
        if self.kerros > target:
            while self.kerros > target:
                self.kerros_alas()
        elif self.kerros < target:
            while self.kerros < target:
                self.kerros_ylös()
        else:
            print(f"Ollaan jo kerroksessa {target}!!")

h = Hissi()


while True:
    p = "dsstjipf"
    # looppaaaaaaa kunnes vastaus on korrekti koska en halua mitää virheitä
    while p not in range(0,11):
        # pidetään se stringinä vaan koska koko paska menee pipareiksi jos laitetaa int() siihen ja käyttäjä antaakin vahingossa kirjaimen tai jotain
        p = input("Anna kerros mihin mennä niin meen sinne yksi kerros kerrallaaan koska tämä on hissi \n uus kerros ------->>> ")
        try:
            p = int(p)
        except ValueError:
            print(f"Anna kerroksen numero et voi antaa mitään '{p}' kerrosta")

    # muutetaa se tässä numeroks koska nyt ollaan päästy veke tuosta looooopista
    h.siirry_kerrokseen(int(p))
