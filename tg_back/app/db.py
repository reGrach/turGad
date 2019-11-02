import MySQLdb
from . import config
from .static import queriesDB


def get_all_stages():
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql = queriesDB.get_all_stages()
    list_stages = []
    try:
        cursor.execute(sql)
        tuple_stages = cursor.fetchall()
        for a in tuple_stages:
            list_stages.append({'value': a[0], 'text': a[1]})
    except MySQLdb.Error as e:
        return "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    finally:
        session.close()
        return list_stages


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


def get_stage_by_id(id):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql = queriesDB.get_stage_by_id(id)
    stage = None
    try:
        cursor.execute(sql)
        res = cursor.fetchone()
        stage = dict(id=res[0], title=res[1], hashcode=res[2])
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    finally:
        session.close()
        return stage


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


def registration_stage(data):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql_reg = queriesDB.reg_stage(data['title'], data['code'])
    sql_get = queriesDB.get_stage_id(data['title'])
    try:
        cursor.execute(sql_reg)
        session.commit()
        try:
            cursor.execute(sql_get)
            res = cursor.fetchone()[0]
        except MySQLdb.Error as e:
            print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
            session.rollback()
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        session.rollback()
        if e.args[0] == 1062:
            res = 'not uniq'
        else:
            res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res


def set_mark(time, id_team, type_mark):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    res = ''
    cursor = session.cursor()
    sql = queriesDB.set_mark(time, id_team, type_mark)
    print(sql)
    try:
        cursor.execute(sql)
        session.commit()
        res = True
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res


def get_f_mark(f_mark):
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    sql = queriesDB.get_f_mark(f_mark)
    try:
        cursor.execute(sql)
        f_mark = cursor.fetchone()[0]
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    finally:
        session.close()
        return f_mark