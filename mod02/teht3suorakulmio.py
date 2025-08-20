a = input("Monta metriä on kannan pituus? ")
b = input("Monta metriä on korkeuden pituus? ")

kanta = float(a)
korkeus = float(b)


alue = kanta * korkeus

piiri = kanta*2 + korkeus*2

print("Teidän pinta-alanne on " + str(alue) + " neliömetriä")

print("Piirinne on " + str(piiri) + " metriä")