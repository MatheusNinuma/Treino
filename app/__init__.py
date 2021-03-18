from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__) #Nome do microblog - cria "new folder" e em seguida "new file"
#__nome__ = python magic - tem características específicas do python

basedir = os.path.abspath(os.abspath.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_sqlalchemy


from app import routes, models #Criando várias "rotas/caminhos" da aplicação
db=SQLAlchemy(app)


#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#import os

#app = Flask(__name__)

#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#from app import routes, models
#db = SQLAlchemy(app)
