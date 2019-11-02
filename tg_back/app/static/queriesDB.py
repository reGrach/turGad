from werkzeug.security import generate_password_hash
from datetime import datetime
from app.api import team


def get_mark_name():
    res = 'SELECT * FROM MarkName'
    return res


def get_all_stages():
    res = 'SELECT * FROM Stages'
    return res


def reg_team(id, name):
    values = [id, name]
    res = 'INSERT INTO Teams (id, name) VALUES ({0[0]}, "{0[1]}")'.format(values)
    return res


def reg_stage(t, c):
    values = [t, generate_password_hash(c, method='sha256')]
    res = 'INSERT INTO Stages (title, hashcode) VALUES("{0[0]}", "{0[1]}")'.format(values)
    return res


def set_mark(time, i, t):
    values = [time, i,  t]
    res = 'INSERT INTO TimeMarks(mark, id_Team, id_MarkName) ' \
          'VALUES("{0[0]}", {0[1]}, {0[2]})'.format(values)
    return res

def get_teamName_by_id(id):
    res = 'SELECT name ' \
          'FROM Teams ' \
          'WHERE id LIKE {0}'.format(id)
    return res


def get_teamName_by_id(id):
    res = 'SELECT name ' \
          'FROM Teams ' \
          'WHERE id LIKE {0}'.format(id)
    return res


# def get_f_mark(id):
#     res = 'SELECT mark ' \
#           'FROM TimeMarks ' \
#           'WHERE id_MarkName LIKE 3'.format(id)
#     return res


def get_stage_by_id(id):
    res = 'SELECT * ' \
          'FROM Stages ' \
          'WHERE id LIKE {0}'.format(id)
    return res


def get_stage_id(title):
    res = 'SELECT id ' \
          'FROM Stages ' \
          'WHERE title LIKE "{0}"'.format(title)
    return res


def get_team_by_id(id):
    res = 'SELECT t.id, t.title, mn.name, tm.mark, s.title ' \
          'FROM Teams AS t ' \
          'JOIN TimeMarks AS tm ON t.id = tm.id_Team ' \
          'JOIN MarkName AS mn ON tm.id_MarkName = mn.id ' \
          'LEFT JOIN Stages AS s ON tm.id_Stage = s.id' \
          'WHERE t.id LIKE {0}'.format(id)
    return res



