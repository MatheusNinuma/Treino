from datetime import datetime #datas e tempo
from app import db #Puxando o Banco de dados

#Duas tabelas do banco de dados
class User(db.Model): #Pego um modelo de tabela base já existente
    id = db.Column(db.Integer, primary_key=True) #Coluna de ID - Chave Primária
    username = db.Column(db.String(64), index=True, unique=True) #Coluna de username
    #email = db.Column(db.String(120), index=True, unique=True) #Não vamos usar e-mail aqui
    password = db.Column(db.String(64)) #Coluna para senha - você nunca vai guardar a senha do cara no bando de dados
    posts = db.relationship('Post', backref='author', lazy='dynamic') 

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model): #Tabela para o POST
    id = db.Column(db.Integer, primar y_key=True) #coluna de id
    body = db.Column(db.String(140)) #O post pode ter no máximo 140 caracteres
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #guarda o horário da postagem
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Guardar

    def __repr__(self):
        return '<Post {}>'.format(self.body)
