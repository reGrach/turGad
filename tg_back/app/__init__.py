from flask import Flask, request
from flask_cors import CORS
from app import config

tur_app = Flask(__name__)

tur_app.config['JSON_AS_ASCII'] = False
tur_app.config['SECRET_KEY'] = config.SECRET_KEY
CORS(tur_app)


@tur_app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response


from app.api import team, stage
