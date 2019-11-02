from flask import Flask
from flask_cors import CORS
from app import config

tur_app = Flask(__name__)

tur_app.config['JSON_AS_ASCII'] = False
tur_app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(tur_app)


@tur_app.route('/api/check')
def check_work():
    return '1'


from app.api import team, stage
