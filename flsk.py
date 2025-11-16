from flask import Flask, request, Response, json, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def moikka():
    return "Hello world!!"

# reitti on http://127.0.0.1:3000/summa?luku1=13&luku2=28
@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summ = luku1+luku2


    # itte tehty jason vastaus
    vastaus = {
        "luku1":luku1,
        "luku2":luku2,
        "summa":summ
    }
    return str(vastaus)


@app.route('/kaiku/<teksti>/<kertaa>')
def kaiku(teksti,kertaa):
    kertaa = int(kertaa)
    vastaukset = []
    for i in range(0,kertaa):
        vastaus = {
            "kaiku" : teksti + " " + teksti
        }
        vastaukset.append(vastaus)
    jsonvast = json.dumps(vastaukset)
    jsonify(vastaukset)

    return Response(response=vastaukset, status=200, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    jsonify(vastaus)
    return Response(response=vastaus, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)