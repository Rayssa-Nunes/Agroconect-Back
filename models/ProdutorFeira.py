from flask_restful import fields
from helpers.database import db

produtor_feira_fields = {
    'produtor_id': fields.Integer,
    'feira_id': fields.Integer,
}

class ProdutorFeira(db.Model):
    __tablename__ = 'tb_produtor_feira'

    produtor_id = db.Column(db.Integer, db.ForeignKey('tb_produtor.id'), primary_key=True)
    feira_id = db.Column(db.Integer, db.ForeignKey('tb_feira.id'), primary_key=True)