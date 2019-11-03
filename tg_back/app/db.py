import MySQLdb
from . import config
from app import queriesDB


# <editor-fold desc="COMMON METHODS">
def insert_to_db(sql):
    res = None
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    try:
        cursor.execute(sql)
        session.commit()
        res = True
    except MySQLdb.Error as e:
        res = 'code error: {0}'.format(e.args[0])
        session.rollback()
    finally:
        session.close()
        return res


def get_from_db(sql, is_one=True):
    res = ''
    session = MySQLdb.connect(
        user=config.DB_USER,
        host=config.DB_HOST,
        passwd=config.DB_PSW,
        db=config.DB_NAME,
        use_unicode=True,
        charset="utf8"
    )
    cursor = session.cursor()
    try:
        cursor.execute(sql)
        if is_one:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
    except MySQLdb.Error as e:
        res = 'code error: {0}'.format(e.args[0])
    finally:
        session.close()
        return res

# </editor-fold>


# <editor-fold desc="TEAM">
def registration_team(id_team, name):
    sql = queriesDB.reg_team(id_team, name)
    return insert_to_db(sql)


def get_team_by_id(id_team):
    sql = queriesDB.get_team_by_id(id_team)
    result_query = get_from_db(sql)
    if isinstance(result_query, str):
        return result_query

    return dict(id=result_query[0], title=result_query[1])

# </editor-fold>


# <editor-fold desc="STAGE">
def registration_stage(title, code):
    sql = queriesDB.reg_stage(title, code)
    return insert_to_db(sql)


def get_all_stages():
    sql = queriesDB.get_all_stages()
    result_query = get_from_db(sql, False)
    if isinstance(result_query, str):
        return result_query

    list_stages = []
    for a in result_query:
        list_stages.append({'value': a[0], 'text': a[1]})
    return list_stages


def get_stage_id_by_title(title):
    sql = queriesDB.get_stage_by_id(title)
    result_query = get_from_db(sql)

    if isinstance(result_query, str):
        return result_query

    return result_query[0]


def get_stage_by_id(id_stage):
    sql = queriesDB.get_stage_by_id(id_stage)
    result_query = get_from_db(sql)

    if isinstance(result_query, str):
        return result_query

    return dict(id=result_query[0], title=result_query[1], hashcode=result_query[2])


# </editor-fold>


# <editor-fold desc="FIXATIONS">
def set_end_fix_to_team(time, id_team, type):
    sql = queriesDB.set_end_fixation(time, id_team, type)
    return insert_to_db(sql)


def get_end_fix_team(id_team, type):
    sql = queriesDB.get_end_fix_team(id_team, type)
    result_query = get_from_db(sql)

    if isinstance(result_query, str):
        return result_query

    return result_query[0]


def get_all_fix_stage_team(id_team):
    sql = queriesDB.get_all_fix_stage_team(id_team)
    result_query = get_from_db(sql, False)

    if isinstance(result_query, str):
        return result_query
    fixs = []
    for fix in result_query:
        fixs.append(dict(time=str(fix[0]), stage=fix[1]))
    return fixs


def send_fix_stages_to_team(time, id_team, id_stage, bonus, fine):
    sql = queriesDB.set_stage_fixation(time, id_team, id_stage, bonus, fine)
    return insert_to_db(sql)

# </editor-fold>




    # sql_get = queriesDB.get_stage_id(data['title'])
    # try:
    #     cursor.execute(sql_reg)
    #     session.commit()
    #     try:
    #         cursor.execute(sql_get)
    #         res = cursor.fetchone()[0]
    #     except MySQLdb.Error as e:
    #         print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    #         res = 'code error: {0}'.format(e.args[0])
    # except MySQLdb.Error as e:
    #     print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    #     session.rollback()
    #     if e.args[0] == 1062:
    #         res = 'not uniq'
    #     else:
    #         res = 'code error: {0}'.format(e.args[0])
    # finally:
    #     session.close()
    #     return res
