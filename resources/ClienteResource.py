from flask import request
from flask_restful import Resource, reqparse, marshal
from models.Cliente import Cliente, cliente_fields
from hash import gera_senha_hash
from helpers.database import db


class ClientesResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome')
        self.parser.add_argument('cpf', type=str, help='Erro no campo cpf', required=True)
        self.parser.add_argument('nascimento', type=str, help='Erro no campo nascimento', required=True)
        self.parser.add_argument('email', type=str, help='Erro no campo email', required=True)
        self.parser.add_argument('senha', type=str, help='Erro no campo senha', required=True)

    def get(self):
        clientes = Cliente.query.all()
        return marshal(clientes, cliente_fields)
    
    def post(self):
        args = self.parser.parse_args()
        try:
            senha_hash = gera_senha_hash(args['senha'])

            novo_cliente = Cliente(
                nome=args['nome'],
                cpf=args['cpf'],
                nascimento=args['nascimento'],
                email=args['email'],
                senha=senha_hash,
            )
            db.session.add(novo_cliente)
            db.session.commit()
            return {'message': 'Cliente criado com sucesso!'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
        

class ClienteResource(Resource):
    parser = reqparse.RequestParser()
    
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome')
        self.parser.add_argument('cpf', type=str, help='Erro no campo cpf')
        self.parser.add_argument('nascimento', type=str, help='Erro no campo nascimento')
        self.parser.add_argument('email', type=str, help='Erro no campo email')
        self.parser.add_argument('senha', type=str, help='Erro no campo senha')

    def get(self, id):
        cliente = Cliente.query.get(id)
        if not cliente:
            return {"message": "Cliente não encontrado"}, 404
        return marshal(cliente, cliente_fields)

    def put(self, id):
        args = self.parser.parse_args()
        cliente = Cliente.query.get(id)
        if not cliente:
            return {'message': 'Cliente não encontrado'}, 404
        
        try:
            if args['nome']:
                cliente.nome = args['nome']
            if args['cpf']:
                cliente.cpf = args['cpf']
            if args['nascimento']:
                cliente.nascimento = args['nascimento']
            if args['email']:
                cliente.email = args['email']
            if args['senha']:
                cliente.senha = gera_senha_hash(args['senha'])
            
            db.session.commit()
            return {'message': 'Cliente alterado com sucesso'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
        
    def delete(self, id):
        cliente = Cliente.query.get(id)
        try:
            db.session.delete(cliente)
            db.session.commit()
            return {'message': 'Cliente deletado com sucesso'}, 200
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500


