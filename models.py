from helpers.database import db

class Usuario(db.Model):
    __tablename__ = 'tb_usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)