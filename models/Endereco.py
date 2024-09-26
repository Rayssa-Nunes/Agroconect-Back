from flask_restful import fields
from helpers.database import db

endereco_fields = {
    'id': fields.Integer,
    'rua': fields.String,
    'numero': fields.Integer,
    'estado': fields.String,
    'cep': fields.String,
    'complemento': fields.String,
    'latitude': fields.Integer,
    'longitude': fields.Integer,
}

class Endereco(db.Model):
    __tablename__ = 'tb_endereco'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rua = db.Column(db.String(255), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    complemento = db.Column(db.String(255))
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)

    def __init__(self, rua, numero, estado, cep, complemento, latitude, longitude):
        self.rua = rua
        self.numero = numero
        self.estado = estado
        self.cep = cep
        self.complemento = complemento
        self.latitude = latitude
        self.longitude = longitude