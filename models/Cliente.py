from flask_restful import fields
from helpers.database import db
from .Usuario import Usuario

cliente_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'cpf': fields.String,
    'nascimento': fields.String,
    'email': fields.String,
}

class Cliente(Usuario):
    __tablename__ = 'tb_cliente'
    
    id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'cliente',
    }

    def __init__(self, nome, cpf, nascimento, email, senha, endereco_id):
        super().__init__(nome=nome, cpf=cpf, nascimento=nascimento, email=email, senha=senha, endereco_id=endereco_id, tipo='cliente')

