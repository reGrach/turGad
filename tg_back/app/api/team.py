from app import tur_app, db
from flask import jsonify, request


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

