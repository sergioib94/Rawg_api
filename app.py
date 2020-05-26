from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

URL_BASE="https://api.rawg.io/api"

@app.route('/',methods=['GET'])
def inicio():
    r=requests.get(URL_BASE + "/games")
    if r.status_code == 200:
        doc=r.json()
        games = []
        for game in doc["results"]:
            games.append(game)
        return render_template("inicio.html", games=games)

app.run(debug=True)
