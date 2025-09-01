print("Anna minulle numeroita. Kerron ovatko ne alkulukuja vai ei. Lopeta välilyönnillä")

# tähän meni jotain puoli tuntia
while True:
    i = input("Anna numero!! ")

    # tarkastetaan onko tyhjä tai välilyönti
    if i.strip() == "":
        break

    #helpottaa kirjoitusta
    num = int(i)
    p = 1
    alku = True

    if num == 1 or num == 0 or num < 0:
        print("kysy jooko jotain vähän isompaa numeroa")
        continue
    # katsotaan onko annettu numero jaollinen millään itseensä asti
    for p in range(2,num):

        # Jos numero on jaollinen MILLÄÄN(paitsi 1) itseään pienemmällä, ei ole alkuluku
        if num % p == 0:
            alku = False
            break
    if alku:
        print(f"{num} on alkuluku!")
    else:
        print(f"{num} ei ole alkuluku!!")