import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def creando_tablas(database):

    sql_create_targetacredito_table = """CREATE TABLE IF NOT EXISTS targetacredito (
                                        id_targetacredito INTEGER PRIMARY KEY AUTOINCREMENT,
                                        banco VARCHAR,
                                        titular VARCHAR,
                                        fecha_caducidad VARCHAR
                                    ); """

    sql_create_productos_table = """ CREATE TABLE IF NOT EXISTS productos (
                                        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR,
                                        marca VARCHAR,
                                        fecha_vencimiento VARCHAR,
                                        precio REAL,
                                        stock INTEGER,
                                        descuento REAL,
                                        descripcion VARCHAR
                                    ); """


    sql_create_ciudad_table = """ CREATE TABLE IF NOT EXISTS ciudad (
                                        id_ciudad INTEGER PRIMARY KEY AUTOINCREMENT,
                                        provincia VARCHAR,
                                        localidad VARCHAR,
                                        departamento VARCHAR
                                    );"""

    sql_create_domicillo_table = """ CREATE TABLE IF NOT EXISTS domicillo (
                                        id_domicillo INTEGER PRIMARY KEY AUTOINCREMENT,
                                        calle1 VARCHAR NOT NULL,
                                        calle2 VARCHAR,
                                        numero INTEGER NOT NULL,
                                        ruta INTEGER,
                                        km INTEGER,
                                        num_depa INTEGER,
                                        piso INTEGER,
                                        id_ciudad INTEGER,
                                        FOREIGN KEY (id_ciudad) REFERENCES ciudad (id_ciudad)
                                    );"""

    sql_create_usuarios_table = """ CREATE TABLE IF NOT EXISTS usuarios (
                                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nombre VARCHAR,
                                        apellido VARCHAR,
                                        usuario VARCHAR,
                                        email VARCHAR,
                                        dni VARCHAR,
                                        tipo VARCHAR,
                                        contraseña VARCHAR,
                                        id_domicillo INTEGER,
                                        FOREIGN KEY (id_domicillo) REFERENCES domicillo (id_domicillo)
                                    );"""
    
    sql_create_comprobantes_table = """CREATE TABLE IF NOT EXISTS comprobante (
                                        id_comprobante INTEGER PRIMARY KEY AUTOINCREMENT,
                                        fecha VARCHAR,
                                        id_targetacredito INTEGER,
                                        id_usuario INTEGER,
                                        FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
                                        FOREIGN KEY (id_targetacredito) REFERENCES targetacredito (id_targetacredito)
                                    ); """

    sql_create_detalles_table = """ CREATE TABLE IF NOT EXISTS detalles (
                                        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                                        id_comprobante INTEGER,
                                        id_producto INTEGER,
                                        cantidad INTEGER,
                                        FOREIGN KEY (id_comprobante) REFERENCES comprobante (id_comprobante),
                                        FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        list_table = [
            "targetacredito",
            "productos",
            "ciudad",
            "domicillo",
            "usuarios",
            "comprobantes",
            "detalles" 
        ]
        # create projects table
        for table in list_table:
            create_table(conn, eval(f"sql_create_{table}_table"))
        print("Tablas creadas")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    creando_tablas("Supermarker.db")
    
