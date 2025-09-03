import math
print("Anna minulle kahden pitsan hinnat sekä halkaisijat senttimetreinä, minä lasken kummasta saa enemmän vastinetta rahalle")

# AIVAN SURKEA TAPA NIMETÄ MUUTTUJIA. EI ENÄÄ KOSKAAN
pizza_arvo = []
pizza_indexer = 0


def pizza(halk, hinta):

    # lasketaan pizzan pinta-ala
    alue = (halk/2) ** 2 * math.pi
    # monta euroa per neliösenttimetri?
    arvo = hinta / alue

    pizza_arvo.append(round(arvo, 2))

    # JOTENKIN VOISI LUULLA ETTÄ OLETUKSEN EI PITÄISI OLLA ETTÄ TULOSTETAAN NUMEROITA 15 MURTOLUVUN TARKKUUDELLA
    print(f"Pizza numero {pizza_indexer} on alueeltaan {round(alue, 2)} cm^2 suuruinen ja arvoltaan {round(arvo, 2)} euroa per cm^2")



for i in range(2):
    pizza_hinta = (float(input(f"Anna pizzan #{i+1} hinta! € ")))
    pizza_halk = (float(input(f"Anna pizzan #{i+1} halkaisija! cm ")))

    pizza_indexer = pizza_indexer + 1
    pizza(pizza_halk, pizza_hinta)

# Etsi pizza_arvo listasta pienin (eli pienin hinta per cm^2) ja ota sen indeksi ja heitä siihen vielä +1 koska emme puhu tietokoneelle
print(f"Pizza #{pizza_arvo.index(min(pizza_arvo))+1} on rahan vastineen kannalta kunkku !!")



