import jwt
from app import tur_app, db, utils
from app.utils import token_required
from flask import request, jsonify, current_app
from datetime import datetime, timedelta


@tur_app.route('/api/stages/login', methods=['POST'])
def login_stage():
    data = request.get_json()
    stage = utils.authenticate(data)
    if not stage:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    token = jwt.encode({
        'id': stage['id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(days=1)},
        current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})


@tur_app.route('/api/stages/getAll', methods=['GET'])
def get_all_stages():
    stages = db.get_all_stages()
    print(stages)
    return jsonify({'result': True, 'stages': stages})


@tur_app.route('/api/stages/registration', methods=['POST'])
def registration_stage():
    data = request.get_json()
    res = db.registration_stage(data)
    if isinstance(res, str):
        return jsonify({'result': False, 'msg': res})
    else:
        return jsonify({'result': True, 'id': res}), 201


@tur_app.route('/api/stages/check', methods=['POST'])
@token_required
def check(stage):
    print(stage)
    return jsonify({'result': True}), 200

