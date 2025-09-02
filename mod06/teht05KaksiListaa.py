import random
print("Teen kaksi listaa täynnä numeroita. Toisesta on parittomat luvut poistettu ")

kaikki = []
parilliset = []


def listat(kk):
    for j in kaikki:
        if j % 2 == 0:
            parilliset.append(j)


    print(f"Alkuperäinen lista on {kaikki}!!")
    print(f"Parillisten numeroiden lista on {parilliset}!!")

for i in range(10):
    num = random.randint(1,10)
    kaikki.append(num)

listat(kaikki)