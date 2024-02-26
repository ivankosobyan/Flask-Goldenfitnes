from app import app
from flask import render_template

from models import Trener,PersonalTrening,GroupTrening

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/trener")
def trener():
    treners = Trener.query.all()
    return render_template("treners.html",treners=treners)

@app.route("/trenings")
def trening():
   grouptrenings=GroupTrening.query.all()

   return render_template("trenings.html",grouptrenings=grouptrenings)

@app.route("/personal_tr")
def personal_tr():
      personal_trenings = PersonalTrening.query.all()
      return render_template("personal_tr.html",personal_trenings=personal_trenings)

@app.route("/trener_personal/<int:trener_id>")
def trener_personal(trener_id):
    trener = Trener.query.get(trener_id)
    personal_trenings = PersonalTrening.query.filter_by(trener_id=trener_id)
    return render_template("trener_personal.html", trener=trener,personal_trenings=personal_trenings)

@app.route("/login")
def login():
    return render_template("login.html")