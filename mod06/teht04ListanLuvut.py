import random
print("Keksin nyt numeroita ja laitan ne listaan ja tulostan niiden summan!! ")
ls = []


def summa(kk):
    # plussataan listan numerot yhteen
    yht = 0
    for j in ls:
        yht += j

    # tulosta lista ja numeroiden summa sekä kohtelias teksti käyttäjälle print-toiminnolla
    print(f"Lista on seuraavanlainen: {ls}!!")
    # tässä tulostetaan listan numeroiden summa :-) minä nimesin summa-muuttujan nimellä yht joka helpottaa koodin -
    # luettavuutta ja ymmärrettävyyttä hieman
    print(f"Listan numerot summattuna on {yht}")

# keksi numeroita ja laita listaan
for i in range(5):
    num = random.randint(1,10)
    ls.append(num)

summa(ls)