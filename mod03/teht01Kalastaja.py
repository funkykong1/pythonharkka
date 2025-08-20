
print("Anna minulle kalastamasi kuhan mitta senttimetreinä. Ilmoitan jos se on alimittainen")
# muuta se saman tien numeroksi johon käy murtoluvut
cm = float(input("Mikä on kalasi mitta? "))

if cm == 37:
    print("Kalasi on pilkulleen alimman pyyntimitan kohdalla!")
elif cm > 37:
    # PYÖRISTÄ desimaaliluvut koska en halua mitään 3.00000003 vastaukseksi!!!
    # kiitos opettaja f string viisaudesta
    print(f"Kalasi mitta on {cm-37:.1f} cm yli pyyntimitan!")
else:
    print(f"Kalasi on {37-cm:.1f} cm liian lyhyt! Laske takaisin veteen")