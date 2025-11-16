from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/')
def moikka():
    return "Hello world!!"


# reitti on http://127.0.0.1:3000/alkuluku/luku
@app.route('/alkuluku/<luku>')
def prime(luku):
    # hei tää näyttää tutulta :O
    num = int(luku)
    alku = True

    if num == 1 or num == 0:
        alku = False
    # katsotaan onko annettu numero jaollinen millään itseensä asti
    if num > 0:
        for p in range(2,num):

            # Jos numero on jaollinen MILLÄÄN(paitsi 1) itseään pienemmällä, ei ole alkuluku
            if num % p == 0:
                alku = False
                break
    else:
        for p in range(-2, num, -1):

            # Jos numero on jaollinen MILLÄÄN(paitsi 1) itseään pienemmällä, ei ole alkuluku
            if num % p == 0:
                alku = False
                break

    # itte tehty jason vastaus
    vastaus = {
        "Number":num,
        "isPrime":alku
    }
    return json.dumps(vastaus)



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
