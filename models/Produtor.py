from flask_restful import fields
from helpers.database import db
from hash import gera_senha_hash, verifica_senha_hash

produtor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'cnpj': fields.String,
    'nascimento': fields.String,
    'propriedade': fields.String,
    'email': fields.String,
}

class Produtor(db.Model):
    __tablename__ = 'tb_produtor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    propriedade = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))

    endereco = db.relationship('Endereco', backref='produtor')
    feira = db.relationship('Feira', secondary='tb_produtor_feira', backref='produtor')

    def __init__(self, nome, cpf, cnpj, nascimento, propriedade, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.cnpj = cnpj
        self.nascimento = nascimento
        self.propriedade = propriedade
        self.email = email
        self.senha = gera_senha_hash(senha)