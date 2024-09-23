from flask import request
from flask_restful import Resource
from models import Usuario
from helpers.database import db

class Register(Resource):
    def post(self):
        data = request.get_json()

        usuario = data.get('usuario')
        email = data.get('email')
        senha = data.get('senha')

        if not usuario or not email or not senha:
            return {'message': 'Campos incompletos', 'type': 'error'}, 400
        
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            return {'message': 'Este usuário já existe', 'type': 'error'}, 400

        novo_usuario = Usuario(usuario=usuario, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        return {'message': 'Usuário registrado com sucesso', 'type': 'success'}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        print(data)

        email = data.get('email')
        senha = data.get('senha')

        if not email or not senha:
            return {'message': 'E-mail e senha são obrigatórios', 'type': 'error'}, 400

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.senha == senha:
            return {'message': 'Login bem-sucedido', 'type': 'success'}, 200
        else:
            return {'message': 'E-mail ou senha incorretos', 'type': 'error'}, 401
