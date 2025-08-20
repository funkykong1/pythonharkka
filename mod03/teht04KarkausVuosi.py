vuosi = int(input("Anna vuosiluku, ilmoitan onko se karkausvuosi "))

# Jaollinen neljällä
if vuosi % 4 == 0:

    # Jaollinen myös sadalla - tarkista onko jaollinen neljälläsadalla myös!!
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("Vuosi " + str(vuosi) + " on karkausvuosi!")
        else:
            print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")

    # Ei jaollinen sadalla - on karkausvuosi
    else:
        print("Vuosi " + str(vuosi) + " on karkausvuosi!")
else:
    print("Vuosi " + str(vuosi) + " ei ole karkausvuosi.")
