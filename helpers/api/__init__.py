from flask_restful import Api
from flask import Blueprint

from resources.ClienteResource import ClientesResource, ClienteResource
from resources.EnderecoResource import EnderecoResource
from resources.FeiraResource import FeiraResource
from resources.ProdutoResource import ProdutoResource
from resources.ProdutorFeiraResource import ProdutorFeiraResource
from resources.ProdutorResource import ProdutoresResource, ProdutorResource
from resources.SetorResource import SetorResource
from resources.LoginResource import LoginResource


blueprint = Blueprint('api', __name__)
api = Api(blueprint, prefix='/api')

api.add_resource(ClientesResource, '/clientes')
api.add_resource(ClienteResource, '/cliente/<int:id>')

api.add_resource(EnderecoResource, '/endereco')
api.add_resource(FeiraResource, '/feira')
api.add_resource(ProdutoResource, '/produto')
api.add_resource(ProdutorFeiraResource, '/produtor_feira')

api.add_resource(ProdutoresResource, '/produtores')
api.add_resource(ProdutorResource, '/produtor/<int:id>')

api.add_resource(SetorResource, '/setor')
api.add_resource(LoginResource, '/login')