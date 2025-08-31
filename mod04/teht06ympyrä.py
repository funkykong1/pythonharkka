import random

total = int(input("Monta pistettä sijoitetaan satunnaisesti neliön alueelle?"))
index = 0
circle_index = 0

x = float(0)
y = float(0)

while index < total:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        circle_index = circle_index + 1
    index = index + 1

likiarvo = 4 * circle_index / index
print(f"Ympyrän sisällä on pisteitä {circle_index} kokonaismäärästä {index}!!")
print(f"Likiarvo on siis täten {likiarvo}!")