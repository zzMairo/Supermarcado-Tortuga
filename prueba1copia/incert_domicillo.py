import sqlite3
from sqlite3 import Error

###------------------------------listo---------------------------------
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


def create_domicillo(conn, domicillo):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO domicillo(calle1, calle2, numero, ruta, km, num_depa, piso, id_ciudad)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, domicillo)
    conn.commit()
    return cur.lastrowid

#calle1, calle2, numero, ruta, km, dem_depa, piso, id_ciudad



def main():
    database = r"Supermarker.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        #producto = ("leche", "sancor", "02-11-2022",200, 100)
        #producto = ("Azucar", "Ledesma", "24-12-2022", 350.5, 250)
        domicillo = [   ("Gina","Puerto",68,208,195.0,96,28,1),
                        ("Mayfield","Sendero",73335,272,199.4,20,14,2),
                        ("Verde","Sur",6,137,222.7,30,25,3),
                        ("Derecho de retención","Sherman",451,189,234.0,2,24,4),
                        ("niño","Springview",583,94,195.4,98,31,5),
                        ("Hoja dorada","Porteo",32550,257,185.6,30,2,6),
                        ("Jenifer","abedul",67,18,217.9,80,25,7),
                        ("Piedra de campo","Gerardo",912,75,176.8,36,2,8),
                        ("Puerto","Arkansas",12942,67,59.5,44,7,9),
                        ("Álamo de Virginia","dispensador",58,235,299.6,1,2,10),
                        ("Algoma","Estrella nueva",1,165,289.4,19,34,11),
                        ("Bahía","tonio",4846,176,226.3,35,1,12),
                        ("Cresta hueca","Amanecer",65675,23,23.5,22,5,13),
                        ("Porteo","Sabio",38985,15,172.3,41,3,14),
                        ("Muir","Una polilla sesenta y cinco",784,74,208.2,98,18,15),
                        ("rosa de la pradera","Portero",4,98,137.6,76,19,16),
                        ("Cresta","brezo Hayes",700,227,38.1,1,6,17),
                        ("abedul","llorón",4070,27,222.0,18,35,18),
                        ("Talmadge","Mandrágora",82,193,109.5,78,15,19),
                        ("anderson","Portero",12927,116,58.0,53,23,20),
                        ("abuela","División",27,296,269.0,91,26,21),
                        ("Dryden","Carpintero",726,41,97,9,32,22),
                        ("Principal","Shopko",4,140,128.9,21,26,23),
                        ("Ala","roja Farragut",580,93,248.8,15,6,24),
                        ("Derecho","retención Puerto Norte",3,29,84.0,43,1,25),
                        ("Hagan","asesino",83,232,12.3,49,31,26),
                        ("ilene","Westerfield",8258,42,65.2,75,17,27),
                        ("ronald","regan arpista",99,44,286.4,85,2,28),
                        ("monumento","Bahía",9,121,281.0,3,4,29),
                        ("Halcón","gris	Noroeste",1072,223,88.2,11,38,30),
                        #("Dorton","Azúcar",583,89,13.3,72,23,31),
                        #("Becker","Centro",606,232,272.2,58,36,32),
                        #("Arapahoe","Fremont",68576,128,59.4,49,31,33),
                        #("Mandrágora","Magdalena",53,43,87.5,20,16,34),
                        #("Esker","Curruca",1,180,130.8,40,14,35),
                        #("Batán","Gerardo",204,30,10.3,60,4036,36),
                        #("Bühler","Spaight",938,218,172.4,87,35,37),
                        #("Alce","Hoepker",7619,29,88.6,70,36,38),
                        #("dispensador","thompson",851,289,277.1,31,34,39)

        ]
        
                    
        create_domicillo(conn,domicillo)


if __name__ == '__main__':
    main()