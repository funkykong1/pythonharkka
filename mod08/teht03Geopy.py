from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
    host="localhost",

    autocommit=True
)

print("Anna minulle kaksi ICAO koodia. Tulostan niiden välisen etäisyyden kilometreinä!!")

ic1 = input("Ensimmäinen: ").upper().strip()
ic1 = f'"{ic1}"'
ic2 = input("Toinen: ").upper().strip()
ic2 = f'"{ic2}"'

cursor = yhteys.cursor()

cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = {ic1}")
lk1 = cursor.fetchone()
cursor.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = {ic2}")
lk2 = cursor.fetchone()



if lk1 is None:
    print(f"Antamasi koodi {ic1} EI vastaa mitään lentokenttää!!")
elif lk2 is None:
    print(f"Antamasi koodi {ic2} EI vastaa mitään lentokenttää!!")
else:
    print(f"Lentokenttien välinen etäisyys on {round(distance.distance(lk1, lk2).kilometers, 2)} KILOMETRIÄ!!!!")
