import MySQLdb
from . import config
from .static import queriesDB


def get():
    session = MySQLdb.connect(
        user=config.DB_USER,
        host='{0}'.format(config.DB_HOST),
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql = queriesDB.get_mark_name()
    list_teams = []
    try:
        cursor.execute(sql)
        tuple_teams = cursor.fetchall()
        for a in tuple_teams:
            list_teams.append(a)
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    finally:
        session.close()
        print(list_teams)
        return list_teams


def get_team_by_id(id):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql = queriesDB.get_teamName_by_id(id)
    team_name = ''
    try:
        cursor.execute(sql)
        team_name = cursor.fetchone()[0]
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    finally:
        session.close()
        return team_name


def registration_team(data):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    res = False
    cursor = session.cursor()
    sql = queriesDB.reg_team(data['id'], data['name'])
    try:
        cursor.execute(sql)
        session.commit()
        res = True
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        session.rollback()
    finally:
        session.close()
        return res