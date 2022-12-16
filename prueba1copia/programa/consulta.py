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


def select_usuario(conn,dato1):#,dato2,dato3):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT nombre, apellido, contraseña FROM usuarios")

    rows = cur.fetchall()

    for row in rows:
        #print(row)
        if row[0]== dato1:#and row[1]==dato2 and row[2]==dato3:
            print(row)
        #else:
         #   print("nombre no encontrado")

def consul():
    database = r"Supermarker.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        #select_usuario_where(conn)
        dato1= str(input("ingrese nombre:"))
        #dato2 = str(input("ingrese apellido:"))
        #dato3= str(input("ingrese contra:"))
        print("2. Query all tasks")
        select_usuario(conn,dato1)#,dato2,dato3)