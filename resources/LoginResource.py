from flask_restful import Resource, reqparse, marshal
from helpers.database import db
from models.Cliente import Cliente, cliente_fields
from models.Produtor import Produtor, produtor_fields
from hash import gera_senha_hash, verifica_senha_hash

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('email', type=str, help='Problema no email', required=True)
        self.parser.add_argument('senha', type=str, help='Problema na senha', required=True)

    def post(self):
        args = self.parser.parse_args()
        email = args["email"]
        senha = gera_senha_hash(args["senha"])
        try:
            cliente = Cliente.query.filter_by(email=email).first()
            if cliente:
                if verifica_senha_hash(cliente.senha, senha):
                    return marshal(cliente, cliente_fields), 200
                else:
                    return {'message': 'Senha incorreta para o cliente'}, 401
                
            produtor = Produtor.query.filter_by(email=email).first()
            if produtor:
                if verifica_senha_hash(produtor.senha, senha):
                    return marshal(produtor, produtor_fields), 200
                else:
                    return {'message': 'Senha incorreta para o produtor'}, 401
                
            return {'message': 'Usuário não encontrado'}, 404
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500