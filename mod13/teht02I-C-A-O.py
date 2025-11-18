import mysql.connector
from flask import Flask, json
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def moikka():
    return "Hello world!!"


# reitti on http://127.0.0.1:3000/airport/icao
@app.route('/airport/<icao>')
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
    cursor.execute(f"SELECT airport.name, airport.municipality, FROM airport WHERE ident = {icao}")
    lk = cursor.fetchall()

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

