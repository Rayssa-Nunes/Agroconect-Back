from flask_restful import fields
from helpers.database import db
from .Usuario import Usuario

produtor_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'cnpj': fields.String,
    'nascimento': fields.String,
    'propriedade': fields.String,
    'email': fields.String,
}

class Produtor(Usuario):
    __tablename__ = 'tb_produtor'

    id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), primary_key=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    propriedade = db.Column(db.String(255), nullable=False)

    feira = db.relationship('Feira', secondary='tb_produtor_feira', backref='produtor')

    __mapper_args__ = {
        'polymorphic_identity': 'produtor',
    }

    def __init__(self, nome, cpf, nascimento, email, senha, cnpj, propriedade, endereco_id):
        super().__init__(nome=nome, cpf=cpf, nascimento=nascimento, email=email, senha=senha, endereco_id=endereco_id, tipo='produtor')
        self.cnpj = cnpj
        self.propriedade = propriedade
