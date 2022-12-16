import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_task(conn, conf):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE productos SET nombre=?, marca=?, fecha_vencimiento=?, precio=? ,stock=?, descuento=?, descripcion=? WHERE id_producto = ?;'''
    cur = conn.cursor()
    cur.execute(sql,conf) #(conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7]))
    conn.commit()
    print("actualizado")


def main():
    database = r"Supermarker.db"

    conf =("mmm","hhhh","2015-01-04",145,14,0,"ssss",1)

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_task(conn,conf)
        print(conf)

if __name__ == '__main__':
    main()