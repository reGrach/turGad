

def get_team_by_id(id):
    # Запрос
    team = {
        'id': 1,
        'title': 'Тестовая',
        'start': '23/10',
        'finish': '24/10',
    }
    if team['id'] == id:
        return team
    else:
        return dict()
