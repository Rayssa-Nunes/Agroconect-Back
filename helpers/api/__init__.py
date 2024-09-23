from flask_restful import Api
from flask import Blueprint

from resources.UsuariosResource import Login, Register

blueprint = Blueprint('api', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')