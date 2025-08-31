import random
print("Minä mietin jotain numeroa 1-10 välillä, koita arvata se!!")

i = random.randint(1,10)

while True:
    vast = int(input("Mikä on veikkauksesi?"))

    if vast == i:
        print(f"Arvasit oikein!! valitsin luvun {i}!")
        quit()

    elif vast > i:
        print(f"{vast} on liian suuri! yritä uudelleen")

    elif vast < i:
        print(f"{vast} on liian pieni! yritä uudelleen")