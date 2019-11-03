import jwt
from app import db, utils
from flask import request, jsonify, current_app
from datetime import datetime, timedelta
from app.utils import get_current_time, token_required
from flask import Blueprint

api = Blueprint("api", __name__)


# <editor-fold desc="API TEAM">
@api.route('/team/registration', methods=['POST'])
def registration_team():
    data = request.get_json()
    res = db.registration_team(data.get('id'), data.get('name'))
    if isinstance(res, str):
        return jsonify({'result': False, 'msg': res})
    else:
        return jsonify({'result': True})


@api.route('/team/get/<int:team_id>', methods=['GET'])
def get_team(team_id):
    team = db.get_team_by_id(team_id)
    if isinstance(team, str):
        return jsonify({'result': False, 'msg': team})
    else:
        team['start'] = db.get_end_fix_team(team_id, 'start')
        team['finish'] = db.get_end_fix_team(team_id, 'finish')
        return jsonify({'result': True, 'team': team})


# @api.route('/team/getUnpassTeam', methods=['GET'])
# @token_required
# def set_finish(stage_id):
#     # Делаем запрос в БД
#     teams = db.get_teams_without_stage(stage_id)
#     if isinstance(teams, str):
#         return jsonify({'result': False, 'msg': teams})
#     else:
#         return jsonify({'result': True, 'teams': teams})

# </editor-fold>


# <editor-fold desc="API STAGE">
@api.route('/stages/login', methods=['POST'])
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


@api.route('/stages/getAll', methods=['GET'])
def get_all_stages():
    stages = db.get_all_stages()
    return jsonify({'result': True, 'stages': stages})


@api.route('/stages/registration', methods=['POST'])
def registration_stage():
    data = request.get_json()
    res = db.registration_stage(data.get('title'), data.get('code'))
    if isinstance(res, str):
        return jsonify({'result': False, 'msg': res})
    else:
        id_stage = db.get_stage_id_by_title(data.get('title'))
        return jsonify({'result': True, 'id': id_stage}), 201
# </editor-fold>


# <editor-fold desc="API FIXATIONS">
@api.route('/fixation/setStart', methods=['POST'])
@token_required
def set_start(id):
    data = request.get_json()
    current_time = get_current_time()
    res = db.set_end_fix_to_team(current_time, data.get('id'), 1)
    if isinstance(res, str):
        return jsonify({'result': False, 'msg': res})
    else:
        return jsonify({'result': True, 'start': current_time})


@api.route('/fixation/setFinish', methods=['POST'])
@token_required
def set_finish(id):
    data = request.get_json()
    current_time = get_current_time()
    res = db.set_end_fix_to_team(current_time, data.get('id'), 2)
    if isinstance(res, str):
        return jsonify({'result': False, 'msg': res})
    else:
        return jsonify({'result': True, 'finish': current_time})

# </editor-fold>
