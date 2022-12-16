import sqlite3
from sqlite3 import Error

###-------------------------listo--------------------
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


def create_usuario(conn, usuario):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO usuarios(nombre, apellido, usuario, email, dni,tipo, contraseña, id_domicillo)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.executemany(sql, usuario)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"Supermarker.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
                    #nombre   apellido   usuario     email                  dni           tipo   contraseña   domicillo
        usuario = [ ("Tierney","Korb","lvernau0","tkorb0@bizjournals.com", "05.608.466","admin","VmMMVJiFh1LP",1),
                    ("Shae","Cliburn","edimitriades1","scliburn1@lycos.com","95.324.967","cliente","4STUdxl",2),
                    ("Ly", "Stubbe", "Lystub","lstubbe2@buzzfeed.com", "42.825.993","admin" ,"JhfMUs",3),
                    ("Marlo", "Cruse","marloc", "mcruse3@vinaora.com", "42.751.597", "cliente","SYfaYb2Zj",4),
                    ("Robby", "Iddiens", "robby12","riddiens4@printfriendly.com", "56.820.422", "cliente","lLu8Z2un",5),
                    ("Jonathan", "Hagard", "jonagard","jhagard5@arizona.edu", "75.854.342","cliente" ,"cdhuQgAVcphP",6),
                    ("haxter", "Fryd", "haxter23","tfryd6@upenn.edu", "00.843.258", "cliente","EjfBK5Tl",7),
                    ("Rip", "Fieldstone","rippiedra", "rfieldstone7@bloglovin.com", "44.485.696", "admin","PPk40gsYt",8),
                    ("Tildie", "Bennit","tildi34" ,"tbennit8@intel.com", "46.636.445","cliente" ,"9oSGHdEWz",9),
                    ("Sabine", "Myrie","sabinemyrie001", "smyrie9@ barnesandnoble.com", "40.821.110","cliente" ,"YfmCvRUec",10),
                    ("Isadora", "Delacourt","isadora_delacourt10" ,"idelacourta@youtube.com", "61.155.218","admin" ,"1apSIj5CgW5L",11),
                    ("Susann", "Stempe", "susann47","sstempeb@cnbc.com", "67.315.326","cliente" ,"vfQzO9dLQ",12),
                    ("Dalia", "Buckingham", "dalia78","dbuckinghamc@bbc.co.uk", "43.633.665", "admin","bxKu5N4",13),
                    ("Jocelyne", "Gadaud","jocelyne_kujo5" ,"jgadaudd@com.com", "43.395.304", "cliente","wBSERCH8J",14),
                    ("Juliette", "Vaneev", "juliette_vane","jvaneeve@over-blog.com", "65.913.932", "cliente","PkrHlS",15),
                    ("Jilly", "Tubridy", "jully2002","jtubridyf@gravatar.com", "26.472.264", "cliente","MpHFiUZ44ahz",16),
                    ("Cami", "Bouskill", "cami_bous7er","cbouskillg@youtube.com", "14.500.308","cliente", "wx9bXXpf",17),
                    ("Jolie", "Laguerre", "jolie1932","jlaguerreh@ifeng.com", "23.895.813", "cliente","c6yrk6t6gU",18),
                    ("Abby", "Theuff", "abby78","atheuffi@printfriendly.com", "20.539.659", "cliente","Tg2CUWZHK",19),
                    ("Kayley", "McClinton","kayley_47", "kmcclintonj@google.com.br", "27.236.988", "cliente","eSXdJxKIT",20),
                    ("Archibaldo", "Seary","archivaldo_archi1" ,"asearyk@instagram.com", "78.731.982","admin", "Gecz9RA8Fgx",21),
                    ("Gwyn", "Pardal","gwyn_pardal56","gpardall@vistaprint.com", "60.957.945","cliente" ,"IpA7F2",22),
                    ("Rutter", "Kellough", "rutter_kellough78","rkelloughm@artisteer.com", "03.020.226", "cliente","GCbCF89Hp3",23),
                    ("Pavia", "Graveston", "pavia_grave2022","pgravestonn@toplist.cz", "72.821.342", "cliente","2B93HGORe",24),
                    ("Margareta", "Leacock", "marg_lecock","mleacocko@home.pl", "28.169.340", "admin","ZxPmYe2R",25),
                    ("Adrianna", "Pegg","adriana_pegg10","apeggp@disqus.com", "30.109.590", "cliente","oyDoVv",26),
                    ("Demetrius", "De Moreno","demetrius45_moreno8" ,"ddemorenoq@zimbio.com", "53.278.926","cliente" ,"uDnUox",27),
                    ("Say", "Mulqueeny", "say_Mul_queen7","smulqueenyr@weebly.com", "25.137.093", "cliente","cxSFrtSaHTX",28),
                    ("Ferdinanda", "Maypother","ferdinan12","fmaypothers@geocities.com", "78.457.239", "admin","tMvFHMA",29),
                    ("Charlene", "Vearncombe", "charlene_v74","cvearncombet@hao123.com", "33.896.159", "cliente","J2bDAm",30)

         ]
        create_usuario(conn, usuario)

if __name__ == '__main__':
    main()
