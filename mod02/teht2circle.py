import math
r = input("Mikä on säteenne pituus?")

## numero joka tulostetaan
rad = 0

## hyväksy vain numerot
if r.isdigit():
    ## muuta teksti numeroksi jotta voidaan laskea sillä
    rad = int(r)
else:
    print("anna numero jatkossa!!")
    quit()

alue = rad ** 2 * math.pi
print("Teidän ympyränne on " + alue)