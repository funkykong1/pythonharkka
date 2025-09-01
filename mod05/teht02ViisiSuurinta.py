print("Anna minulle numeroita. Kirjaan ne kaikki ja tulostan lopuksi viisi suurinta!! lopeta ohjelma välilyönnillä")

lista = []

while True:
    i = input("Anna numero!! ")

    # tarkastetaan onko tyhjä tai välilyönti
    if i.strip() == "":
        break
    else:
        #miten pitäisi tietää tästä ilman googlea?? append????? miten olisi ADD
        lista.append(int(i))

lista.sort(reverse=True)
print("Tässä on suurimmat luvut listassa alkaen suurimmasta!")

#mennään koko listan läpi siten että ei tule virheitä vaikka olisikin alle 5 numeroa listassa.
# len????? 
for j in range(len(lista)):
    if j == 5:
        break
    print(lista[j])
