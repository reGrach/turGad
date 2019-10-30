from flask import Flask
from flask_cors import CORS


tur_app = Flask(__name__)
CORS(tur_app)

from app.api import team, stage

