import random
print("Keksin nyt numeroita ja laitan ne listaan ja tulostan niiden summan!! ")
ls = []


def summa(kk):
    # plussataan listan numerot yhteen
    yht = 0
    for j in ls:
        yht += j

    print(f"Lista on seuraava: {ls}!!")
    print(f"Listan numerot summattuna on {yht}")

# keksi numeroita
for i in range(5):
    num = random.randint(1,10)
    ls.append(num)

summa(ls)