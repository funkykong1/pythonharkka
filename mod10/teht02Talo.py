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



# pähee systeemi
# muuttaa jutun annetuksi tyypiksi jos se toimii ja muuten valittaa käyttäjälle
def INPUT_VIRHE_SKANNAAJA_ONKO_OIKEA_TYYPPI(inputti, annettu_typpi):
    try:
        output = annettu_typpi(inputti)
    except ValueError:
        print(f"Vastaus ei kelpaa anna sellainen jonka haluan se ois {annettu_typpi}")
    else:
        return output

# parempi kun että joutuisi laittamaan tän koko homman joka kerta kun kysytään jotain
def kysy_pelaajalta_asiaa_kunnes_vastaa_oikein(teksti, oikeet_vastaukset):
    inp = ""
    while inp not in oikeet_vastaukset:
        inp = input(teksti)
        inp = INPUT_VIRHE_SKANNAAJA_ONKO_OIKEA_TYYPPI(inp, type(oikeet_vastaukset[0]))
    return inp

talon_ylin = kysy_pelaajalta_asiaa_kunnes_vastaa_oikein("Mikä saisi olla talon kerroksien lukumäärä", range(1,100))
talon_hissit = kysy_pelaajalta_asiaa_kunnes_vastaa_oikein("Mikä saisi olla talon hissien lukumäärä", range(1,100))

talo = Talo(talon_hissit, 0, talon_ylin)


while True:
    # looppaaaaaaa kunnes vastaus on korrekti koska en halua mitää virheitä
    hissi_integer_tunniste_nro = kysy_pelaajalta_asiaa_kunnes_vastaa_oikein(
        f"\nhissejä on {len(talo.hissit)}. valitse yksi niistä (1, 2, 3...)\n hissi valinta ------->>> ",
        range(1, len(talo.hissit) + 1),
    )
    # hissi on nyt hissi objekti talon listoilta
    hissi = talo.hissit[hissi_integer_tunniste_nro - 1]

    # uus looppi jossa katotaan kerros
    targetti_kerros = "taas"
    while targetti_kerros not in range(0, talo.ylin + 1):

        targetti_kerros = input(f"\nkerroksia on {talo.ylin}. hissinne on kerroksessa {hissi.kerros} \n uuus kerros ------->>> ")
        try:
            targetti_kerros = int(targetti_kerros)
        except ValueError:
            print(f"Anna kerroksen numero et voi antaa mitään '{targetti_kerros}' kerrosta")


    talo.aja_hissiä(hissi, targetti_kerros)

