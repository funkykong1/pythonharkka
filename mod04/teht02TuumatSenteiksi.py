print("Anna tuumien määrä, muutan ne senteiksi. Anna negatiivinen luku lopettaaksesi ohjelman ")

tuumat = 1

while tuumat > 0:
    tuumat = float(input("Monta tuumaa? "))
    if tuumat > 0:
        print(f"{tuumat} Tuumaa on sentteinä {tuumat*2.54} cm!")
    else:
        print("Hyvästi!")
