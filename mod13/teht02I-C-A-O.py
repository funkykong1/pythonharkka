import mysql.connector
from flask import Flask, json
import json

app = Flask(__name__)


@app.route('/')
def moikka():
    return "Hello world!!"
icao = "efhk"

# reitti on http://127.0.0.1:5000
@app.route('/kentta/<icao>')
def kaakao(icao):

    yhteys = mysql.connector.connect(
        port=3306,
        host="localhost",
        database="flight_game",
        user='vilho',
        password='chmv',
        autocommit=True
    )

    cursor = yhteys.cursor()
    # HAE country sekä airport hakemistoista kaikki relevantti tieto lentokentästä.
    cursor.execute(f"select name, municipality from airport where ident = '{icao}'")
    lk = cursor.fetchone()


    name = lk[0]
    region = lk[1]


    # itte tehty jason vastaus
    vastaus = {
        "ICAO": icao,
        "Name": name,
        "Municipality": region
    }
    return json.dumps(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

