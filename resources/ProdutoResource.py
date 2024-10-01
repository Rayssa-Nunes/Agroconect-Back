from flask_restful import Resource, marshal_with, reqparse
from models.Produto import Produto, produto_fields
from helpers.database import db

class ProdutoResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome', required=True)
        self.parser.add_argument('preco', type=int, help='Erro no campo preço', required=True)
        self.parser.add_argument('descricao', type=str, help='Erro no campo descrição')
        self.parser.add_argument('imagem', type=str, help='Erro no campo imagem')

    @marshal_with(produto_fields)
    def get(self):
        produtos = Produto.query.all()
        return produtos
    
    def post(self):
        args = self.parser.parse_args()
        try:
            novo_produto = Produto(
                nome = args['nome'],
                preco = args['preco'],
                descricao = args['descricao'],
                imagem = args['imagem'],
            )

            db.session.add(novo_produto)
            db.session.commit()

            return {'message': 'Produto cadastrado com sucesso!'}, 201
        except Exception as e:
            return {'message': str(e)}, 500