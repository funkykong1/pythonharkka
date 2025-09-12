import mysql.connector

yhteys = mysql.connector.connect(
    port = 3306,
    host="localhost",
    database="flight_game",
    user="vilho",
    password="chmv",
    autocommit=True
)

cursor = yhteys.cursor() #emt mutta tämä antaa suorittaa komentoja

cursor.execute("SELECT type FROM airport") # suorittaa komennon

res = cursor.fetchall() # tuo yhden tuloksen joukosta, oletuksena aakkosjärjestys

for i in range(300):
    print(res[i])
