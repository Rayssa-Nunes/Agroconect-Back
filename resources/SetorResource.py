from flask import request
from flask_restful import Resource, marshal_with, reqparse
from models.Setor import Setor, setor_fields
from helpers.database import db

class SetorResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Erro no campo nome', required=True)

    @marshal_with(setor_fields)
    def get(self):
        setores = Setor.query.all()
        return setores
    
    def post(self):
        args = self.parser.parse_args()
        try:
            novo_setor = Setor(
                nome = args['nome']
            )

            db.session.add(novo_setor)
            db.session.commit()

            return {'message': 'Setor cadastrado com sucesso!'}, 201
        except Exception as e:
            return {'message': str(e)}, 500