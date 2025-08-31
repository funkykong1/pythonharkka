
print("Minulla on tiedossa käyttäjätunnus. Anna minulle tunnus sekä salasana !!")

user = "python"
word = "rules"

attempts = 5

while attempts > 0:
    vast_user = input("Mikä on käyttäjätunnus?")
    vast_word = input("Mikä on salasana?")

    if vast_user == user and vast_word == word:
        print("Tervetuloa herra python!!")
        quit()

    else:
        attempts = attempts - 1
        print(f"Väärät tunnukset, yrityksiä jäljellä {attempts}")

print("Vastasit väärin viisi kertaa! Pääsy Evätty!")