from app import tur_app, db
from flask import jsonify, request
from ..utils import get_current_time

@tur_app.route('/api/team/registration', methods=['POST'])
def registration_team():
    data = request.get_json()
    res = db.registration_team(data)
    if res:
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})


@tur_app.route('/api/team/get/<int:team_id>')
def get_team_name(team_id):
    # Делаем запрос в БД
    team = db.get_team_by_id(team_id)
    if team == '':
        return jsonify({'result': False})
    else:
        return jsonify({'result': True, 'title': team})


@tur_app.route('/api/team/<int:team_id>/setStart')
def get_start(team_id):
    current_time = get_current_time()
    # Делаем запрос в БД
    res_mark = db.set_mark(current_time, team_id, 1)
    if isinstance(res_mark, str):
        return jsonify({'result': False, 'msg': res_mark})
    else:
        return jsonify({'result': True, 'time': current_time})


@tur_app.route('/api/team/<int:team_id>/setFinish')
def get_finish(team_id):
    current_time = get_current_time()
    # Делаем запрос в БД
    res_mark = db.set_mark(current_time, team_id, 3)
    if isinstance(res_mark, str):
        return jsonify({'result': False, 'msg': res_mark})
    else:
        return jsonify({'result': True, 'time': current_time})