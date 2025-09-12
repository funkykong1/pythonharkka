import mysql.connector
from collections import Counter

yhteys = mysql.connector.connect(
    port = 3306,
    host="localhost",
    database="flight_game",
    user="vilho",
    # super salainen älä lue :p
    password="chmv",
    autocommit=True
)

ic = input(print("Anna minulle maan koodi, kerron monta erilaista lentokenttää maassa sijaitsee!!! \n esim: FI \n ->")).upper().strip()
ic = f'"{ic}"'

cursor = yhteys.cursor()
# HAE country sekä airport hakemistoista kaikki relevantti tieto lentokentästä.

cursor.execute(f"SELECT type FROM airport WHERE iso_country = {ic}")
lk = cursor.fetchall()

if lk:
    # jumalan siunaus
    print(f"{Counter(lk)}")
else:
    print("En löytänyt mitään tätä koodia vastaavaa maata!!")
