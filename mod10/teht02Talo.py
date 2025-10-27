class Talo:
    def __init__(self, hissit = 1, alin = 0, ylin = 10):
        self.hissit = []
        for hi in range(0,hissit):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

        self.alin = alin
        self.ylin = ylin

    def aja_hissiä(self, hissi, kerros):
        hissi.siirry_kerrokseen(kerros)




class Hissi:
    def __init__(self, alin = 0, ylin = 10):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
            print(f"Menty ylös yksi kerros. Uusi kerros on {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
            print(f"Menty alas yksi kerros. Uusi kerros on {self.kerros}")

    def siirry_kerrokseen(self, target):
        if self.kerros > target:
            while self.kerros > target:
                self.kerros_alas()
        elif self.kerros < target:
            while self.kerros < target:
                self.kerros_ylös()
        else:
            print(f"Ollaan jo kerroksessa {target}!!")

talon_ylin = int(input("mikä ois talon ylin kerrosluku"))
talon_hissit = int(input("mikä saisi olla talon hissien lukumäärä"))
talo = Talo(talon_hissit, 0, talon_ylin)

while True:
    hissi_integer_tunniste_nro = "dsstjipf"
    # looppaaaaaaa kunnes vastaus on korrekti koska en halua mitää virheitä
    while hissi_integer_tunniste_nro not in range(1, len(talo.hissit) + 1):
        # pidetään se stringinä vaan koska koko paska menee pipareiksi jos laitetaa int() siihen ja käyttäjä antaakin vahingossa kirjaimen tai jotain
        hissi_integer_tunniste_nro = input(f"\nhissejä on {len(talo.hissit)}. valitse yksi niistä (1, 2, 3...)\n hissi valinta ------->>> ")
        try:
            hissi_integer_tunniste_nro = int(hissi_integer_tunniste_nro)
        except ValueError:
            print(f"Anna elevaattorin numero et voi antaa mitään hissiä numero '{hissi_integer_tunniste_nro}'")
    # hissi on nyt hissi objekti talon listoilta
    hissi = talo.hissit[hissi_integer_tunniste_nro - 1]

    # uus looppi jossa katotaan kerros
    targetti_kerros = "taas"
    while targetti_kerros not in range(0, talo.ylin + 1):
        # pidetään se stringinä vaan koska koko paska menee pipareiksi jos laitetaa int() siihen ja käyttäjä antaakin vahingossa kirjaimen tai jotain
        targetti_kerros = input(f"\nkerroksia on {talo.ylin}. hissinne on kerroksessa {hissi.kerros} \n uuus kerros ------->>> ")
        try:
            targetti_kerros = int(targetti_kerros)
        except ValueError:
            print(f"Anna kerroksen numero et voi antaa mitään '{targetti_kerros}' kerrosta")

    # muutetaa se tässä numeroks koska nyt ollaan päästy veke tuosta looooopista
    talo.aja_hissiä(hissi, targetti_kerros)
