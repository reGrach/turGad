from flask import Flask
from flask_cors import CORS
from app import config
from .api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = config.SECRET_KEY
    CORS(app)

    @app.route("/")
    def index():
        return "Hello"

    @app.route('/check')
    def check_work():
        return '1'
    return app
