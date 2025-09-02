import random
print("Heitän nyt noppaa funktion avulla kunnes tulee silmäluvuksi 6")


def heitto():
    noppa = 0
    while noppa != 6:
        noppa = random.randint(1,6)
        print(f"Silmäluvuksi tuli {noppa}!!")


heitto()