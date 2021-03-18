from flask import Flask 

app = Flask(__name__) #Nome do microblog - cria "new folder" e em seguida "new file"
#__nome__ = python magic - tem características específicas do python

from app import routes #Criando várias "rotas/caminhos" da aplicação



