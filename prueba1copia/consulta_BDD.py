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


def select_usuario(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT nombre, apellido, contraseña FROM usuarios")

    rows = cur.fetchall()
    #print(rows)
    for row in rows:
        print(row)
        #if row[0]== dato:
         #   print(row)
        #else:
         #   print("nombre no encontrado")


#def select_usuario_where(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    #cur = conn.cursor()
    #cur.execute("SELECT* FROM usuarios WHERE nombre='Rip';") #WHERE nombre=?", (priority,))

    #rows = cur.fetchall()

    #for row in rows:
        #if "Rip"== row:
            #print(row)



def main():
    database = r"Supermarker.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        #select_usuario_where(conn)
        #dato = str(input("ingrese nombre:"))
        print("2. Query all tasks")
        select_usuario(conn)


if __name__ == '__main__':
    main()