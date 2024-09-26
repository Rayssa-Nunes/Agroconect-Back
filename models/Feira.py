from flask_restful import fields
from helpers.database import db

feira_fields = {
    'id': fields.Integer,
    'nome': fields.String,
}

class Feira(db.Model):
    __tablename__ = 'tb_feira'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))

    endereco = db.relationship('Endereco', backref='feira')

    def __init__(self, nome):
        self.nome = nome