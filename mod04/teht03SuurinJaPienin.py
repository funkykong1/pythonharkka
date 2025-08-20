print("Anna minulle lukuja niin pitkään kuin sielu sietää. Lopeta ohjelma välilyönnillä. Kerron lopuksi suurimman ja pienimmän antamasi luvun ")

# Tehdään siitä teksti jotta voidaan hyödyntää strip() toimintoa
i = "1"

pienin = 0
suurin = 0

#lukujen kokonaismäärä
index = 0

# tee ikuinen toisto josta
while True:
    i = input("Anna seuraava numero! ")

    if i.strip() == "":
        break

    if float(i) > suurin:
        suurin = float(i)
    elif float(i) < pienin:
        pienin = float(i)
    index += 1

print(f"Annoit {index} numeroa yhteensä. Näistä suurin oli {suurin} ja pienin {pienin}!!")