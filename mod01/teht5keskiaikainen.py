## 20 naulaa - 8512g
leiv = int(input("Anna leiviskät "))
## 32 luotia - 425.6g
naula = int(input("Anna naulat "))
## 13.3 grammaa
luoti = int(input("Anna luodit! "))

## muunna kaikki grammoiksi
leiv = leiv * 8512
naula = naula * 425.6
luoti = luoti * 13.3

gram = leiv+naula+luoti

## joka tuhannes gramma lisätään +1kg
kg = 0
for i in range(0, int(gram-1000), 1000):
    kg += 1

## jakojäännöksellä selvitetään grammojen määrä
gram = gram % 1000

print("Sinulla on kilogrammoja " + str(kg) + " ja grammoja " + str(gram))

