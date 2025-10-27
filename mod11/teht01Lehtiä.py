class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    # tää ei kyllä ole sen vaivan arvoista tässä
    def tulosta_tiedot(self):
        print(f"Julkaisun nimi on {self.nimi}, ", end='')

class Kirja(Julkaisu):
    def __init__(self, nimi, tekijä, sivut):
        super().__init__(nimi)
        self.sivut = sivut
        self.tekijä = tekijä


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjailija {self.tekijä}, sivuja {self.sivut}.")

class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.tekijä = toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittaja {self.tekijä}.")


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti Nro 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()

