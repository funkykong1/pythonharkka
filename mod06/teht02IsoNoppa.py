import random
print("Heitän nyt noppaa funktion avulla kunnes tulee nopan suurin silmäluku")

nop = int(input("Miten iso noppanne on? "))

def heitto(koko):

    noppa = 0
    while noppa != koko:
        noppa = random.randint(1,koko)
        print(f"Silmäluvuksi tuli {noppa}!!")


heitto(nop)