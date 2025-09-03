print("Muunnan galloonat litroiksi teille. Anna negatiivinen luku lopettaaksesi ohjelman !!!! \nSuutun jos annat jotain muuta kun numeron")

#yksinkertaisesti muuntaa ja tulostaa
def muunnos(gl):
        gl = gl * 3.785
        print(f"Sinulla on litroja {round(gl , 2)}!!")

#toista kokoajan kunnes tulee negatiivinen vastaus
while True:
    gal = input("Miten monta yhdysvaltalaista galloonaa polttoainetta on? ")

    # aivan mahtava tapa tehdä tämä
    try:
        float(gal)
    except ValueError:
        print(f"'{gal}' ei ole numero >:/")
        continue

    Vilhon_siisti_numero = float(gal)

    if Vilhon_siisti_numero < 0:
        print("Hyvästi!")
        break

    # tee siitä FLOAT jotta se toimii murtolukulaskuissa
    muunnos(Vilhon_siisti_numero)