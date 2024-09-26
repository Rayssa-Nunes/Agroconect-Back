from flask import request
from flask_restful import Resource, marshal_with, reqparse
from models import Feira
from models.Feira import feira_fields
from helpers.database import db

class FeiraResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('nome', type=str, help='Informe o campo "Nome" corretamente', required=True)

    @marshal_with(feira_fields)
    def get(self):
        feiras = Feira.query.all()
        return feiras
    
    def post(self):
        args = self.parser.parse_args()
        try:
            nova_feira = Feira(
                nome = args['nome']
            )

            db.session.add(nova_feira)
            db.session.commit()

            return {'message': 'Feira adicionada com sucesso!'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500