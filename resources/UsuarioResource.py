from flask_restful import Resource, reqparse, marshal
from models.Usuario import Usuario, usuario_fields
from models.Cliente import Cliente
from models.Produtor import Produtor
from helpers.database import db
from hash import gera_senha_hash


class UsuariosResource(Resource):
    parser = reqparse.RequestParser()

    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome')
        self.parser.add_argument('cpf', type=str, help='Erro no campo cpf')
        self.parser.add_argument('cnpj', type=str, help='Erro no campo cnpj')
        self.parser.add_argument('nascimento', type=str, help='Erro no campo nascimento')
        self.parser.add_argument('propriedade', type=str, help='Erro no campo propriedade')
        self.parser.add_argument('email', type=str, help='Erro no campo email')
        self.parser.add_argument('senha', type=str, help='Erro no campo senha')
        self.parser.add_argument('tipo', type=str, help='Erro no campo tipo')

    def get(self):
        usuarios = Usuario.query.all()
        return marshal(usuarios, usuario_fields), 200
    
    def post(self):
        args = self.parser.parse_args()
        tipo = args['tipo']
        try:
            senha_hash = gera_senha_hash(args['senha'])

            if tipo == 'cliente':
                novo_cliente = Cliente(
                nome = args['nome'],
                cpf = args['cpf'],
                nascimento = args['nascimento'],
                email = args['email'],
                senha = senha_hash,
                )

                db.session.add(novo_cliente)
                db.session.commit()

                return {'message': 'Cliente cadastrado com sucesso'}, 201
            elif tipo == 'produtor':
                novo_produtor = Produtor(
                    nome = args['nome'],
                    cpf = args['cpf'],
                    nascimento = args['nascimento'],
                    email = args['email'],
                    senha = senha_hash,

                    cnpj=args['cnpj'],
                    propriedade=args['propriedade']
                )

                db.session.add(novo_produtor)
                db.session.commit()

                return {'message': 'Produtor cadastrado com sucesso'}, 201
            
            else:
                return {'message': 'Tipo de usuário inválido'}, 400
            
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500