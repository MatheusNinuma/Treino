#Nesse arquivo, a gente vai colocar as nossas rotas
#essas rotas dependem do app

from app import app 
from flask import render_template #Arquivo HTML


@app.route("/")  #Para essa URL, acontece a função a seguir
@app.route("/index") #Duas URL para a mesma página
def index():
    return render_template("index.html") #toda vez que a pessoa entrar nessa página, devolve esse html
#    return "Olá, mundo"


