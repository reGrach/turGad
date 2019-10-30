from datetime import datetime


def get_mark_name():
    res = 'SELECT * FROM MarkName'
    return res


def reg_team(id, name):
    values = [id, name]
    res = 'INSERT INTO Teams (id, name) VALUES ({0[0]}, "{0[1]}")'.format(values)
    return res

def get_teamName_by_id(id):
    res = 'SELECT name ' \
          'FROM Teams ' \
          'WHERE id LIKE {0}'.format(id)
    return res


def get_team_by_id(id):
    res = 'SELECT t.id, t.title, mn.name, tm.mark, s.title ' \
          'FROM Teams AS t ' \
          'JOIN TimeMarks AS tm ON t.id = tm.id_Team ' \
          'JOIN MarkName AS mn ON tm.id_MarkName = mn.id ' \
          'LEFT JOIN Stages AS s ON tm.id_Stage = s.id' \
          'WHERE t.id LIKE {0}'.format(id)
    return res

