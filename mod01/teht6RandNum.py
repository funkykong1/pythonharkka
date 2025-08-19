import random
num = 0
koodi1 = ""
koodi2 = ""

for i in range(0,3):
    num = random.randint(0,9)
    koodi1 += str(num)


for i in range(0,4):
    num = random.randint(1,6)
    koodi2 += str(num)


print("Ensimmäinen koodinne on " + koodi1 + "! \n")
print("Toinen koodinne on " + koodi2 + "!")