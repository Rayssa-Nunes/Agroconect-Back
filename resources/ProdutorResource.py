from flask import request
from flask_restful import Resource, reqparse, marshal
from models.Produtor import Produtor, produtor_fields
from helpers.database import db
from hash import gera_senha_hash

from psycopg2.errors import UniqueViolation


class ProdutoresResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome', required=True)
        self.parser.add_argument('cpf', type=str, help='Erro no campo cpf', required=True)
        self.parser.add_argument('cnpj', type=str, help='Erro no campo cnpj', required=True)
        self.parser.add_argument('nascimento', type=str, help='Erro no campo nascimento', required=True)
        self.parser.add_argument('propriedade', type=str, help='Erro no campo propriedade', required=True)
        self.parser.add_argument('email', type=str, help='Erro no campo email', required=True)
        self.parser.add_argument('senha', type=str, help='Erro no campo senha', required=True)

    def get(self):
        produtores = Produtor.query.all()
        return marshal(produtores, produtor_fields)
    
    def post(self):
        args = self.parser.parse_args()
        try:
            novo_produtor = Produtor(
                nome = args['nome'],
                cpf = args['cpf'],
                cnpj = args['cnpj'],
                nascimento = args['nascimento'],
                propriedade = args['propriedade'],
                email = args['email'],
                senha = gera_senha_hash(args['senha'])
            )

            db.session.add(novo_produtor)
            db.session.commit()

            return {'message': 'Produtor cadastrado com sucesso!'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
        
class ProdutorResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome')
        self.parser.add_argument('cpf', type=str, help='Erro no campo cpf')
        self.parser.add_argument('cnpj', type=str, help='Erro no campo cnpj')
        self.parser.add_argument('nascimento', type=str, help='Erro no campo nascimento')
        self.parser.add_argument('propriedade', type=str, help='Erro no campo propriedade')
        self.parser.add_argument('email', type=str, help='Erro no campo email')
        self.parser.add_argument('senha', type=str, help='Erro no campo senha')

    def get(self, id):
        produtor = Produtor.query.get(id)
        if not produtor:
            return {"message": "Produtor não encontrado"}, 404
        return marshal(produtor, produtor_fields)

    def put(self, id):
        args = self.parser.parse_args()
        produtor = Produtor.query.get(id)
        if not produtor:
            return {'message': 'Produtor não encontrado'}, 404
        
        try:
            if args['nome']:
                produtor.nome = args['nome']
            if args['cpf']:
                produtor.cpf = args['cpf']
            if args['cnpj']:
                produtor.cnpj = args['cnpj']
            if args['nascimento']:
                produtor.nascimento = args['nascimento']
            if args['propriedade']:
                produtor.propriedade = args['propriedade']
            if args['email']:
                produtor.email = args['email']
            if args['senha']:
                produtor.senha = args['senha']
            
            db.session.commit()
            return {'message': 'Produtor alterado com sucesso'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
        
    def delete(self, id):
        produtor = Produtor.query.get(id)
        try:
            db.session.delete(produtor)
            db.session.commit()
            return {'message': 'Produtor deletado com sucesso'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500