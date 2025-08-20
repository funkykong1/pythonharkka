import math
r = input("Mikä on säteenne pituus metreinä?")

# numero joka tulostetaan
rad = 0

# hyväksy vain numerot
if r is float or int:
    # muuta teksti numeroksi jotta voidaan laskea sillä
    rad = float(r)
else:
    print("anna numero jatkossa!!")
    quit()

alue = rad ** 2 * math.pi
print("Teidän ympyränne on alueeltaan " + str(alue) + " neliömetriä")