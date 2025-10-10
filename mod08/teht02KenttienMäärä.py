import mysql.connector
from collections import Counter

yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,

    autocommit=True
)

ic = input("Anna minulle maan koodi, kerron monta erilaista lentokenttää maassa sijaitsee!!! \n esim: FI \n --> ").upper().strip()
ic = f'"{ic}"'

cursor = yhteys.cursor()

cursor.execute(f"SELECT type FROM airport WHERE iso_country = {ic}")
lk = cursor.fetchall()

if lk:
    # jumalan siunaus
    print(f"{Counter(lk)}")
else:
    print("En löytänyt mitään tätä koodia vastaavaa maata!!")
