from app import tur_app, db


@tur_app.route('/team/qr/<int:team_id>')
def registration(team_id):
    # Делаем запрос в БД
    team = db.get_team_by_id(team_id)
    if team == {}:
        return {}
    else:
        return team