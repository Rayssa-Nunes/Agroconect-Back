from flask_restful import fields
from helpers.database import db
from hash import gera_senha_hash, verifica_senha_hash

cliente_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'nascimento': fields.String,
    'email': fields.String,
}

class Cliente(db.Model):
    __tablename__ = 'tb_cliente'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))

    endereco = db.relationship('Endereco', backref='cliente')

    def __init__(self, nome, cpf, nascimento, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.senha = gera_senha_hash(senha)


