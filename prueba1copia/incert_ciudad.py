import sqlite3
from sqlite3 import Error

###-------------------------------------listo------------------------------------
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


def create_ciudad(conn, ciudad):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO ciudad(provincia, localidad, departamento)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, ciudad)
    conn.commit()
    return cur.lastrowid





def main():
    database = r"Supermarker.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        #producto = ("leche", "sancor", "02-11-2022",200, 100)
        #producto = ("Azucar", "Ledesma", "24-12-2022", 350.5, 250)
        ciudad = [  ("Buenos Aires","Abasto","La Plata"),	
                    ("Catamarca","Bañado de Ovanta","Santa Rosa"),
                    ("Chaco","Colonia Popular","Libertad"),
                    ("Chubut","Comodoro Rivadavia","Escalante"),
                    ("Córdoba","Alicia","San Justo"),
                    ("Corrientes","Colonia Pando","San Roque"),
                    ("Entre Rios","Aldea San Juan","Paraná"),
                    ("Formosa","Formosa","Formosa"),
                    ("Jujuy","Colonia San José","Tilcara"),
                    ("La Pampa","Doblas","Atreuco"),
                    ("La Rioja","Guanchin","Chilecito"),
                    ("Mendoza","Barrio La Pega","Lavalle"),
                    ("Misiones","San Javier","San Javier"),
                    ("Neuquén","Varvarco","Minas"),
                    ("Río Negro","El Bolsón","Bariloche"),	
                    ("Salta","Cerrillos","Cerrillos"),
                    ("Salta","Iruya","Iruya"),
                    ("Salta","Cafayate","Cafayate"),
                    ("Salta","Santa Rosa de los Pastos Grandes","Los Andes"),
                    ("Salta","La Merced","Cerrillos"),
                    ("Salta","Isla de Cañas","Iruya"),
                    ("Salta","Tolar Grande","Los Andes"),
                    ("Salta","La Merced","Cerrillos"),
                    ("Salta","Tolombóm","Cafayate"),
                    ("Salta","Ceibalito","Anta"),
                    ("Salta","Río Piedras","Metán"),
                    ("Salta","Lumbreras","Metán"),
                    ("Salta","Cobres","La Poma"),
                    ("San Juan","Guanacache","Sarmiento"),
                    ("La Rioja","Guanquill","Chilecito")


        ]
        
                    
        create_ciudad(conn,ciudad)


if __name__ == '__main__':
    main()