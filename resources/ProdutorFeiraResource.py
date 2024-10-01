from flask_restful import Resource, marshal_with, reqparse
from models.ProdutorFeira import ProdutorFeira, produtor_feira_fields
from helpers.database import db

class ProdutorFeiraResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('produtor_id', type=int, help='Erro no campo relação com produtor', required=True)
        self.parser.add_argument('feira_id', type=int, help='Erro no campo relação com feira')

    @marshal_with(produtor_feira_fields)
    def get(self):
        produtores_feiras = ProdutorFeira.query.all()
        return produtores_feiras
    
    def post(self):
        args = self.parser.parse_args()
        try:
            novo_produtor_feira = ProdutorFeira(
                produtor_id = args['produtor_id'],
                feira_id = args['feira_id']
            )

            db.session.add(novo_produtor_feira)
            db.session.commit()

            return {'message': 'Nova relação produtor-feira cadastrada com sucesso!'}, 201
        except Exception as e:
            return {'message': str(e)}, 500