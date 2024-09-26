from flask_restful import fields
from helpers.database import db

setor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
}

class Setor(db.Model):
    __tablename__ = 'tb_setor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=True)