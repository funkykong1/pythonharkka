# muuta annettu teksti isoksi ei tarvitte käyttäjän välittää asiasta
hytti = input("Anna laivan hyttiluokka, saat sanallisen kuvauksen hytin laadusta ").upper()

if hytti == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella!!")
elif hytti == "A":
    print("A-luokan hytti on ikkunallinen hytti autokannen yläpuolella!")
elif hytti == "B":
    print("B-luokan hytti on ikkunaton hytti autokannen yläpuolella")
elif hytti == "C":
    print("C-luokan hytti on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka!!")