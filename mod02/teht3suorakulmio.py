a = input("Mikä on kannan pituus?")
b = input("Mikä on korkeuden pituus?")

kanta = int(a)
korkeus = int(b)


alue = kanta * korkeus

piiri = kanta*2 + korkeus*2

print("Teidän pinta-alanne on " + str(alue))
print("Piirinne on " + str(piiri))