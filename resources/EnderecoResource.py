from flask import request
from flask_restful import Resource, marshal_with, reqparse
from models import Endereco
from models.Endereco import endereco_fields
from helpers.database import db

class EnderecoResource(Resource):
    parser = reqparse.RequestParser()
    def __init__(self):
        self.parser.add_argument('rua', type=str, help='Informe o campo "Rua"', required=True)
        self.parser.add_argument('numero', type=int, help='Informe o campo "Número"', required=True)
        self.parser.add_argument('estado', type=str, help='Informe o campo "Estado"', required=True)
        self.parser.add_argument('cep', type=str, help='Informe o campo "Cep"', required=True)
        self.parser.add_argument('complemento', type=str, help='Informe o campo "Cep"')
        self.parser.add_argument('latitude', type=int, help='Informe o campo "Latitude"', required=True)
        self.parser.add_argument('longitude', type=int, help='Informe o campo "Longitude"', required=True)

    @marshal_with(endereco_fields)
    def get(self):
        enderecos = Endereco.query.all()
        return enderecos
    
    def post(self):
        args = self.parser.parse_args()
        try:
            novo_endereco = Endereco(
                rua=args['rua'],
                numero=args['numero'],
                estado=args['estado'],
                cep=args['cep'],
                complemento=args['complemento'],
                latitude=args['latitude'],
                longitude=args['longitude']
            )
            db.session.add(novo_endereco)
            db.session.commit()
            return {'message': 'Endereço criado com sucesso!'}, 201
        except Exception as e:
            db.session.rollback()
            return {'message': str(e)}, 500
