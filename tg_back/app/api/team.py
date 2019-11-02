from app import tur_app, db
from flask import jsonify, request
from ..utils import get_current_time, token_required


@tur_app.route('/api/team/registration', methods=['POST'])
def registration_team():
    data = request.get_json()
    res = db.registration_team(data)
    if res:
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})


@tur_app.route('/api/team/get/<int:team_id>', methods=['GET'])
def get_team_name(team_id):
    # Делаем запрос в БД
    team = db.get_team_by_id(team_id)
    if isinstance(team, str):
        return jsonify({'result': False, 'msg': team})
    else:
        if team is None:
            title = db.get_title_team_by_id(team_id)
            if title:
                team = dict(title=title)
            else:
                return jsonify({'result': False})
        return jsonify({'result': True, 'team': team})


@tur_app.route('/api/team/setStart', methods=['POST'])
@token_required
def set_start(id):
    data = request.get_json()
    print(data)
    current_time = get_current_time()
    # Делаем запрос в БД
    res_mark = db.set_mark(current_time, data.get('id'), 1)

    if isinstance(res_mark, str):
        return jsonify({'result': False, 'msg': res_mark})
    else:
        return jsonify({'result': True, 'start': current_time})


@tur_app.route('/api/team/setFinish', methods=['POST'])
@token_required
def set_finish(id):
    team_id = request.get_json()['id']
    current_time = get_current_time()
    # Делаем запрос в БД
    res_mark = db.set_mark(current_time, team_id, 3)
    if isinstance(res_mark, str):
        return jsonify({'result': False, 'msg': res_mark})
    else:
        return jsonify({'result': True, 'finish': current_time})