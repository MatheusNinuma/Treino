#Nesse arquivo, a gente vai colocar as nossas rotas
#essas rotas dependem do app

from app import app 
from flask import render_template, request #Arquivo HTML


@app.route("/")  #Para essa URL, acontece a função a seguir
@app.route("/index") #Duas URL para a mesma página
def index():
    user = {'username': 'Matheus'}
    posts = [
        {'autor': {'username': 'Aline'}, 'body': "Olá da Maria"},
        {'autor': {'username': 'Ricardo'}, 'body': "Olá!"}
    ]
    return render_template("index.html", user=user, posts=posts) #toda vez que a pessoa entrar nessa página, devolve esse html
#    return "Olá, mundo", envia a variável username

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.values.get("user"), request.values.get("pass"), request.values.get("remember"))
    return render_template("login.html" , title="Login")

