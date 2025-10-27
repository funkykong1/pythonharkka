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

print("PALOHÄLYTYS!!!!! KAIKKI HISSIT ALAS HETI!!!!!!!")

for hiz in talo.hissit:
    hiz.siirry_kerrokseen(0)
