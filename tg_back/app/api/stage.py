from app import tur_app
from flask import request


@tur_app.route('/hello', methods=['GET'])
def hello():
    id = request.args.get('id')
    print(id)
    return id