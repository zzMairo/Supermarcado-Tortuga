import sqlite3
from sqlite3 import Error

###----------------------------------------listo-----------------------------------
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


def create_productos(conn, producto):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO productos(nombre, marca, fecha_vencimiento, precio, stock, descuento, descripcion)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, producto)
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
        producto = [("Chicken Half","laferre","1/7/2022",117,10,0,"pollo cosinado 1.5kg sin guarnicion"),
                    ("Alcaparras","campo arta","7/6/2022",275,65,0,"alcaparras encurtidas baja calorias"),
                    ("Rape - Fresco","sant bell","5/15/2022",268,11,0,"pescado fresco 1kg"),
                    ("Vino - Tinto", "Harrow Estates","16/4/2022",175,103,0,"vino tinto 1lt"),
                    ("Chalotes","zaparra","11/3/2022",294,102,0,"challote bolsa de 1kg"),
                    ("Langosta - Bebé","hervante","15/6/2022",255, 128,0,"langosta de 2kg de chile"),
                    ("Limonada","Calypso","17/04/2022",91,125,0,"limonada 2lt sin gas"),
                    ("Almendras Molidas","Blaqueda","26/03/2022",202,158,0,"bolsa de almendras 500gr"),
                    ("Pan","Baquette Francés","03/12/2021",54,80,0,"1kg de pan "),
                    ("Durazno Seco","el duraznon","9/ 8/2022",274,71,0,"durazno fresco 1kg "),
                    ("Papas Fritas","Reggy","1/27/2022",101,56,0," papas fritas 500gr Reggy 20cl"),
                    ("Nuez Moscada","Molinda","3/6/2022",260,118,0,"nuez moscada 20gm"),
                    ("Vino - blanco","Ej Gallo Valle Sierra","1/31/2022",275,144,0,"vino blanco 1lt "),
                    ("Pan - Multigrano","el amanecer","11/2/2022",233,137,0,"pan multigrano 1kg"),
                    ("Res","Montreal Smoked","8/24/2022",297,166,0,"1kg de res al vacio"),
                    ("Cappucino Mix","Island Oasis","6/2/2022",106,94,0,"capuchino mix sobre de 5gr"),
                    ("Queso - Cheddar","Old White","26/1/2022",264,128,0,"queso chedar 500gr"),
                    ("Queso - Suizo","Oka","9/11/2022",204,27,0,"queso suizo 500gr"),
                    ("Queso - Romano","rallendro","2/6/2022",117,156,0,"queso romano 500gr"),
                    ("Vino - blanco","Chateau Bonnet","7/24/2022",225.50,192,0," vino blanco 1lt"),
                    ("leche","Herb Du Provence","11/8/2022",68.67,27,0,"leche 1lt 0cl"),
                    ("Carne de res","Primerba","9/28/2022",174.76,26,0,"carne de res 1kg al vacio"),
                    ("leche-almendra","sermix","6/6/2022",65.17,192,0,"leche de almendra 1lt"),
                    ("Res","Magarita","11/23/2022",110.69,186,0,"carne de res al vacion 1kg"),
                    ("Col Roll","Island Oasis","7/10/2022",251.85,65,0,""),
                    ("Repollo","Napa","28/11/2021",171.95,194,0," repollo 1kg"),
                    ("Miel","Lavangra","2/12/2021",296.51,182,0,"miel de abeja 500lt"),
                    ("Extracto - Limón","limsim","28/6/2022",277.54,4,0,"extracto de limon 500lt "),
                    ("Trufa","Pap Bulco","18/11/2022",245.96,108,0," bolsa de trufas 500kg "),
                    ("Chocolate - Semi Dulce","Calets","16/1/2022",135.99,37,0,"chocolate semi dulce 250kg"),
                    ("Tarta De Pera Francesa","lourent","10/1/2022",243.49 ,57,0,"tarta  de pera francesa 500kg"),
                    ("Trufa","rapt light","17/3/2022",174.58,116,0,"bolsa de trufas 500kg"),
                    ("gelatina - mazana","Momiji Oroshi","13/6/2022",147.49,145,0,"sobre de gelatina de manzana 150gr"),
                    ("Atún - Fresco","Chili Sauce","16/10/2022",83.18,174,0,"atun fresco 1kg"),
                    ("Vino - Malbec","Trapiche","8/4/2022",81.35,147,0," vino malbec 1lt"),
                    ("Cerveza","Mill St Organic","6/30/2022",70.88,22,0,"cerveza 1lt"),
                    ("pasta - tallarin","Shiro Miso","1/1/2022",57.29,27,0,"pasta de tallarin 250kg"),
                    ("gaseosa - cola","Frangelico","5/4/2022",278.23,101,0,"gaseosa sabor cola 1lt"),
                    ("Sopa - Cebolla Francesa","Secaa","5/21/2022",141.84,163,0,""),
                    ("Harina - Garbanzos","grand lop","6/24/2022",123.51,200,0,"gaseosa sabor naranja 1lt"),
                    ("gaseosa - naranja","Whmis Spray","4/14/2022",175.60,145,0,"gaseosa sabor naranja 1lt"),
                    ("Salsa - Soya","Graduada","1/19/2022",87.95,168,0,"Salsa - Soya 1lt"),
                    ("Aceitunas - Rellenas","la promm","6/2/2022",95.98,138,0,"Aceitunas - Rellenas 250kg"),
                    ("Berenjenas - Baby","la cocecha","9/22/2022",110.74,194,0,"berenjenas 1kg"),
                    ("Barra - Chocolate Dulce Y Salado","chocolit","5/23/2022",189.79,50,0,"Barra - Chocolate Dulce Y Salado 500kg"),
                    ("Galleta - salada","Amaretto","8/4/2022",192.95,62,0,"Galleta - salada 250kg por 3"),
                    ("Pasta - Black Olive","","9/21/2022",208.78,9,0,"Pasta - Black Olive 250kg"),
                    ("Salsa - Black Current","Dry Mix","9/3/2022",196.49,133,0,"salsa black current 500lt"),
                    ("gaseosa - mora","Squash Butternut","2/25/2022",222.38,62,0,"gaseosa sabor naranja 1lt"),
                    ("Pasta de Trufa","la proont","6/4/2022",176.41 ,184,0,"Pasta de Trufa"),
                    ("Cangrejo","pess mar","10/31/2022",286.17,99,0,"cangrejo por 3"),
                    ("Lechuga - Romaine","la cocecha","6/24/2022",259.40,132,0,"Lechuga - Romaine 1kg"),
                    ("gelatina - naranja","Canada Dry","7/31/2022",50.14,21,0,"gelatina - naranja 25kg"),
                    ("Harina","del 4oz","19/2/2022",160.22,192,0,"harina 1kg"),
                    ("Vino - blanco","Ej Gallo Sierra Valley","31/10/2022",258.07,107,0,"Vino - blanco 1lt"),
                    ("tortilla","Super Clar","13/6/2022",171.94,151,0,"tortilla sin tacc por 5"),
                    ("Semillas de Fenngreek","semilla loca","15/7/2022",169.75,48,0,"Semillas de Fenngreek 500kg"),
                    ("Helado -vainilla","Ice Clear","8/4/2022",144.81,185,0,"Helado -vainilla  3lt"),
                    ("Salsa - Bernaise","serMix","15/1/2022",164.96,132,0,"Salsa - Bernaise 1lt"),
                    ("Pan - Maíz Muffaleta","Cebollaenta","30/7/2022",203.64,41,0,"Pan - Maíz Muffaleta  1kg")
        ]
                   
        
        
                    
        create_productos(conn, producto)


if __name__ == '__main__':
    main()