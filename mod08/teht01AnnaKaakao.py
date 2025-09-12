import mysql.connector

yhteys = mysql.connector.connect(
    port = 3306,
    host="localhost",
    database="flight_game",
    user="vilho",
    # super salainen älä lue :p
    password="chmv",
    autocommit=True
)

# en tiedä miksi tämä tulostaa none!!!!!!!!!
ic = input(print("Anna minulle yhden lentokentän ICAO-koodi, etsin lentokentän nimen ja sijainnin teille.")).upper().strip()
ic = f'"{ic}"'

cursor = yhteys.cursor()
# HAE country sekä airport hakemistoista kaikki relevantti tieto lentokentästä.
cursor.execute(f"SELECT airport.name, country.name, country.continent FROM airport, country WHERE ident = {ic}")
lk = cursor.fetchone()
if lk:
    print(f"Hakemanne vastaa lentokenttää {lk[0]} maassa {lk[1]} joka sijaitsee mantereella {lk[2]}!!!")
else:
    print("En löytänyt mitään tätä koodia vastaavaa lentokenttää!!")
