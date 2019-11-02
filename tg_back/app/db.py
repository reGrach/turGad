import MySQLdb
from . import config
from app import queriesDB


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
    sql = queriesDB.get_team_by_id(id)
    res = None
    try:
        cursor.execute(sql)
        team_info = cursor.fetchall()
        marks = []
        start = ''
        finish = ''
        for it in team_info:
            if it[1] == 2:
                marks.append(dict(time=str(it[2]), stage=it[3]))
            elif it[1] == 1:
                start = str(it[2])
            elif it[1] == 3:
                finish = str(it[2])
        res = dict(title=team_info[0][0], start=start, finish=finish, marks=marks)
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res


def get_title_team_by_id(id):
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
    res = None
    try:
        cursor.execute(sql)
        res = cursor.fetchone()[0]
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res


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
    res = None
    try:
        cursor.execute(sql)
        stage = cursor.fetchone()
        res = dict(id=stage[0], title=stage[1], hashcode=stage[2])
    except MySQLdb.Error as e:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
        res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res


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
        res = 'code error: {0}'.format(e.args[0])
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
            res = 'code error: {0}'.format(e.args[0])
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
        session.rollback()
    finally:
        session.close()
        return res
