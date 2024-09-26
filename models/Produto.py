from flask_restful import fields
from helpers.database import db


produto_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'preco': fields.Integer,
    'descricao': fields.String,
    'imagem': fields.String,
}

class Produto(db.Model):
    __tablename__ = 'tb_produto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=True)
    preco = db.Column(db.Integer, nullable=True)
    descricao = db.Column(db.String(255))
    imagem = db.Column(db.String(255))
    setor_id = db.Column(db.Integer, db.ForeignKey('tb_setor.id'))
    produtor_id = db.Column(db.Integer, db.ForeignKey('tb_produtor.id'))

    setor = db.relationship('Setor', backref='produto')
    produtor = db.relationship('Produtor', backref='produto')

    def __init__(self, nome, preco, descricao, imagem):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.imagem = imagem
        