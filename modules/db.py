import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_cook(conn, cook):
    """
    Create a new cookid
    :param conn:
    :param cookid:
    :return:
    """

    sql = """ INSERT INTO cooklist(date,starttime,endtime,description)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, cook)
    return cur.lastrowid


def log_data(conn, logitem):
    """
    Log data from cook
    :param conn:
    :param cookid:
    :param timestamp:
    :param probe1_temp:
    :param grate_temp:
    :param fan_on:
    :param fan_speed:
    :return:
    """

    sql = """ INSERT INTO cooklog(cookid,timestamp,probe1_temp,grate_temp,fan_on,fan_speed)
              VALUES(?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, logitem)
    return cur.lastrowid
