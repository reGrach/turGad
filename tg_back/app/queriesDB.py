from werkzeug.security import generate_password_hash


# <editor-fold desc="TEAM">
def reg_team(id_team, name):
    values = [id_team, name]
    return 'INSERT INTO Teams (id, name) VALUES ({0[0]}, "{0[1]}")'.format(values)


def get_team_by_id(id_team):
    return 'SELECT * FROM Teams WHERE id LIKE {0}'.format(id_team)

# </editor-fold>

# <editor-fold desc="STAGE">
def reg_stage(t, c):
    values = [t, generate_password_hash(c, method='sha256')]
    return 'INSERT INTO Stages (title, hashcode) VALUES("{0[0]}", "{0[1]}")'.format(values)


def get_stage_by_id(id_stage):
    return 'SELECT * FROM Stages WHERE id LIKE {0}'.format(id_stage)


def get_all_stages():
    return 'SELECT id, title FROM Stages'


# </editor-fold>

# <editor-fold desc="FIXATIONS">


def set_end_fixation(time, i, t):
    values = [time, i,  t]
    return 'INSERT INTO Fixations(mark, id_Team, id_MarkName) ' \
           'VALUES("{0[0]}", {0[1]}, {0[2]}'.format(values)


def set_stage_fixation(time, i, t, ist, b, f):
    values = [time, i,  t, ist, b, f]
    return 'INSERT INTO Fixations(mark, id_Team, id_MarkName, id_Stage, bonus, fine) ' \
           'VALUES("{0[0]}", {0[1]}, 3, {0[3]}, {0[4]}, {0[5]})'.format(values)


def get_all_fix_stage_team(id_team):
    return 'SELECT f.mark, s.title, f.bonus, f.fine ' \
           'FROM Teams AS t ' \
           'JOIN Fixations AS f ON t.id = f.id_Team ' \
           'JOIN Stages AS s ON f.id_Stage = s.id ' \
           'WHERE t.id LIKE {0}'.format(id_team)


def update_stage_bonus(id_team, id_stage, bonus):
    values = [id_team, id_stage, bonus]
    return 'UPDATE Fixations.bonus ' \
           'SET bonus = {0[2]} ' \
           'WHERE id_team={0[0]} and id_stage={0[1]}'.format(values)


def get_end_fix_team(id_team, type):
    values = [id_team, type]
    return 'SELECT f.mark,  ' \
           'FROM Teams AS t ' \
           'JOIN Fixations AS f ON t.id = f.id_Team ' \
           'JOIN FixationTypes AS ft ON f.id_FixationType = ft.id ' \
           'WHERE t.id LIKE {0[0]} AND ft.name LIKE {0[1]}'.format(values)


# </editor-fold>




# def get_team_by_id(id):
#     res = 'SELECT t.name AS "TeamName", mn.id, tm.mark, s.title AS "stageName" ' \
#           'FROM Teams AS t ' \
#           'JOIN TimeMarks AS tm ON t.id = tm.id_Team ' \
#           'JOIN MarkName AS mn ON tm.id_MarkName = mn.id ' \
#           'LEFT JOIN Stages AS s ON tm.id_Stage = s.id ' \
#           'WHERE t.id LIKE {0}'.format(id)
#     return res
#
#
# def get_teams_without_stage(id):
#     res = 'SELECT t.name AS "TeamName", mn.id, tm.mark, s.title AS "stageName" ' \
#           'FROM Teams AS t ' \
#           'JOIN TimeMarks AS tm ON t.id = tm.id_Team ' \
#           'JOIN MarkName AS mn ON tm.id_MarkName = mn.id ' \
#           'LEFT JOIN Stages AS s ON tm.id_Stage = s.id ' \
#           'WHERE t.id LIKE {0}'.format(id)
#     return res
