from flask_restful import Resource, reqparse, marshal
from helpers.database import db
from models.Cliente import Cliente, cliente_fields
from models.Produtor import Produtor, produtor_fields
from models.Usuario import Usuario
from hash import gera_senha_hash, verifica_senha_hash

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('email', type=str, help='Problema no email', required=True)
        self.parser.add_argument('senha', type=str, help='Problema na senha', required=True)

    def post(self):
        args = self.parser.parse_args()
        email = args["email"]
        senha = args["senha"]
        try:
            usuario = Usuario.query.filter_by(email=email).first()
            if not usuario:
                return {'message': 'Usuário não encontrado'}, 404
            
            if not verifica_senha_hash(usuario.senha, senha):
                return {'message': 'Senha incorreta'}, 401
            
            if usuario.tipo == 'cliente':
                cliente = Cliente.query.filter_by(id=usuario.id).first()
                return marshal(cliente, cliente_fields), 200
            if usuario.tipo == 'produtor':
                produtor = Produtor.query.filter_by(id=usuario.id).first()
                return marshal(produtor, produtor_fields), 200
            else:
                return {'message': 'Tipo de usuário desconhecido'}, 400
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
