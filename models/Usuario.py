from flask_restful import fields
from helpers.database import db

usuario_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'nascimento': fields.String,
    'email': fields.String,
    'tipo': fields.String,
}

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nascimento = db.Column(db.Date)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey('tb_endereco.id'))
    tipo = db.Column(db.String(50))

    endereco = db.relationship('Endereco', backref='usuario')

    __mapper_args__ = {
        'polymorphic_identity': 'usuario',
        'polymorphic_on': tipo,
    }

    def __init__(self, nome, cpf, nascimento, email, senha, tipo, endereco_id):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.endereco_id = endereco_id
