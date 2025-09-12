print("Anna minulle nimiä. Kerron onko se sanottu jo aikaisemmin vai ei \nLopeta ohjelma tyhjällä !!")
nimet = set()

#yksinkertainen while mikä menee pois kun annetaan tyhjä
while True:
    # title toiminto tekee nimistä pakosti Isolla Alkukirjaimella alkavia ja sivuuttaa huolet annettujen kirjainten koosta
    nimi = input("Anna seuraava nimi ").title()

    #välilyönti tai välimerkki lopettaa ja tulostaa nimet
    if nimi.strip() == "":
        print(f"Sinun nimilistasi on: {nimet}")
        break
        
    #uusi = True
    uusi = True

    for n in nimet:
        if nimi == n:
            print(f"{nimi} on jo listassa!")
            uusi = False
            break

    if uusi:
        print(f"{nimi} ei ollut vielä listassa!")
        nimet.add(nimi)