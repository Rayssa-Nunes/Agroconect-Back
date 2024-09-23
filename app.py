from flask import Flask
from helpers.database import db
from helpers.api import blueprint
from helpers.cors import cors

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

cors.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.register_blueprint(blueprint)

db.init_app(app) 

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
