from app import app
from flask import render_template,redirect,url_for
from forms import LoginForm,RegisterForm
from models import Trener,PersonalTrening,GroupTrening,User
from db import db
from flask_login import login_user,login_required,logout_user
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

@app.route("/login",methods=["GET","POST"])
def login():
    message = ""
    form = LoginForm()
    if form.is_submitted():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first() # first() ищет первое совпадение
        if user is not None and user.hashed_password == password:
            message = "Авторизация осуществленна"
            login_user(user)
        else:
            message = "Неверный логин или пароль"

    return render_template("login.html", form=form,message=message)

@app.route("/register",methods=["GET","POST"])
def register():
    message = ""
    form = RegisterForm()
    if form.is_submitted(): # проверка для запуска формы
        email= form.email.data
        password = form.password.data
        password_repeat= form.password_repeat.data
        print(email,password,password_repeat)
        print("Данные")
        
        if User.query.filter_by(email=email).first() is not None:
            message = "Пользователь с таким email уже существует!"
        elif password != password_repeat:
            message = "Пароли должны совпадать!"
        else:
            u = User(email=email,hashed_password=password)
            db.session.add(u)
            db.session.commit()
            message = "Поздравляю вы счастливый пользователь нашего сайта, ждите рекламной рассылке на почту =)"

    return render_template("register.html",form=form,message=message)


@app.route("/lms")
@login_required
def lms():


    return render_template("lms.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))



@app.errorhandler(500)
def error_500(e):
    return render_template("500.html"),500

@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"),404

@app.errorhandler(401)
def error_401(e):
    return render_template("401.html"),401


