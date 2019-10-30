from flask import Flask

tur_app = Flask(__name__)
from app.api import team, stage

