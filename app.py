from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

URL_BASE="https://api.rawg.io/api"

@app.route('/',methods=['GET','POST'])
def inicio():
    if request.method=='GET':
        r=requests.get(URL_BASE + "/games")
        if r.status_code == 200:
            doc=r.json()
            games = []
            for game in doc['results']:
                games.append(game)
            return render_template("inicio.html", games=games)
    else:
        nombre=request.form.get("name")
        payload = {'search' : nombre}
        r=requests.get(URL_BASE + "/games", params=payload)
        if r.status_code == 200:
            doc2=r.json()
            datos = []
            for juego in doc2['results']:
                datos.append(juego)
            return render_template("busqueda.html", datos=datos)

@app.route('/<slug>',methods=['GET'])
def juego(slug):
    r=requests.get(URL_BASE + "/games/" + slug)
    if r.status_code == 200:
        doc3=r.json()
        return render_template("juego.html",juego=doc3)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=False)
