from app import tur_app, db
from flask import jsonify, request


@tur_app.route('/team/registration', methods=['POST'])
def registration():
    data = request.get_json()
    res = db.registration_team(data)
    if res:
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})


@tur_app.route('/team/get/<int:team_id>')
def get_team_name(team_id):
    # Делаем запрос в БД
    team = db.get_team_by_id(team_id)
    if team == '':
        return jsonify({'result': False})
    else:
        return jsonify({'result': True, 'title': team})


@tur_app.route('/mark')
def mark():
    # Делаем запрос в БД
    team = db.get()
    return jsonify(team)

