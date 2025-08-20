print("Kerro sukupuolesi sekä hemoglobiiniarvosi niin kerron onko arvosi kohdillaan!!")

# taas tee tekstistä pakosti kokonaan pieni, voidaan suoraan verrata if-lausekkeissa
sukup = input("Mikä on sukupuolesi? (mies/nainen) ").lower()
hemo = int(input("Mikä on hemoglobiiniarvosi? (kokonaislukuna g/l) "))

yla = 0
ala = 0

#aseta rajat ja tulosta niiden perusteella
if sukup == "mies":
    yla = 195
    ala = 134

elif sukup == "nainen":
    yla = 175
    ala = 117

else:
    print("Virheellinen sukupuoli :/")



if hemo > yla:
    print("Hemoglobiiniarvosi " + str(hemo) + " g/l on korkea! Ylärajanne on " + str(yla) + " g/l")

elif hemo < ala:
    print("Hemoglobiiniarvosi " + str(hemo) + " g/l on alhainen! Alarajanne on " + str(ala) + " g/l")

else:
    print("Hemoglobiiniarvosi" + str(hemo) + " g/l on normaali! Ylärajanne on " +  str(yla) + " g/l ja alaraja " + str(ala) + " g/l.")

