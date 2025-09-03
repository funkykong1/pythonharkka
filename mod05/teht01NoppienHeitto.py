import random
nopat = int(input("Anna minulle numero, heitän tämän numeron verran noppia ja kerron silmäluvut!! "))
luvut = 0

for i in range(nopat):
    # randint sisällyttää molemmat ei tarvii mitään 0 ja 7
    num = random.randint(1,6)
    luvut += num

print(f"{nopat} noppaa heitetty joiden summa {luvut}!!")