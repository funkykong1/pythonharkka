import random
print("Minä mietin jotain numeroa väliltä 1-10, koita arvata se!!")

i = random.randint(1,10)

while True:
    vast = int(input("Mikä on veikkauksesi?"))

    if vast == i:
        print(f"Arvasit oikein!! valitsin luvun {i}!")

    elif vast > i:
        print(f"{vast} on liian korkealla! yritä uudelleen")

    elif vast < i:
        print(f"{vast} on liian matala! yritä uudelleen")