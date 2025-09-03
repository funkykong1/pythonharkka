print("Anna minulle kaupunkien nimiä VIISI KAPPALETTA..... Minä toistan ne sinulle :-)")

kaikki = []
# tismalleen viisi eikä yhtään enempää
for p in range(5):
    kaikki.append(input("Anna kaupungin nimi minulle !!"))

# mennään listan läpi ja tulostetaan vähän nimiä
for kp in kaikki:
    print(kp)


