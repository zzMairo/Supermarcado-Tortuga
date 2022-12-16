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
    sql = ''' INSERT INTO usuarios(nombre, apellido, email, dni, contraseña, id_domicillo)
              VALUES(?,?,?,?,?,?) '''
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
        usuario = [ ("Tierney","Korb","tkorb0@bizjournals.com", "05.608.466","VmMMVJiFh1LP",1),
                    ("Shae","Cliburn","scliburn1@lycos.com","95.324.967","4STUdxl",2),
                    ("Ly", "Stubbe", "lstubbe2@buzzfeed.com", "42.825.993", "JhfMUs",3),
                    ("Marlo", "Cruse", "mcruse3@vinaora.com", "42.751.597", "SYfaYb2Zj",4),
                    ("Robby", "Iddiens", "riddiens4@printfriendly.com", "56.820.422", "lLu8Z2un",5),
                    ("Jonathan", "Hagard", "jhagard5@arizona.edu", "75.854.342", "cdhuQgAVcphP",6),
                    ("haxter", "Fryd", "tfryd6@upenn.edu", "00.843.258", "EjfBK5Tl",7),
                    ("Rip", "Fieldstone", "rfieldstone7@bloglovin.com", "44.485.696", "PPk40gsYt",8),
                    ("Tildie", "Bennit", "tbennit8@intel.com", "46.636.445", "9oSGHdEWz",9),
                    ("Sabine", "Myrie", "smyrie9@ barnesandnoble.com", "40.821.110", "YfmCvRUec",10),
                    ("Isadora", "Delacourt", "idelacourta@youtube.com", "61.155.218", "1apSIj5CgW5L",11),
                    ("Susann", "Stempe", "sstempeb@cnbc.com", "67.315.326", "vfQzO9dLQ",12),
                    ("Dalia", "Buckingham", "dbuckinghamc@bbc.co.uk", "43.633.665", "bxKu5N4",13),
                    ("Jocelyne", "Gadaud", "jgadaudd@com.com", "43.395.304", "wBSERCH8J",14),
                    ("Juliette", "Vaneev", "jvaneeve@over-blog.com", "65.913.932", "PkrHlS",15),
                    ("Jilly", "Tubridy", "jtubridyf@gravatar.com", "26.472.264", "MpHFiUZ44ahz",16),
                    ("Cami", "Bouskill", "cbouskillg@youtube.com", "14.500.308", "wx9bXXpf",17),
                    ("Jolie", "Laguerre", "jlaguerreh@ifeng.com", "23.895.813", "c6yrk6t6gU",18),
                    ("Abby", "Theuff", "atheuffi@printfriendly.com", "20.539.659", "Tg2CUWZHK",19),
                    ("Kayley", "McClinton", "kmcclintonj@google.com.br", "27.236.988", "eSXdJxKIT",20),
                    ("Archibaldo", "Seary", "asearyk@instagram.com", "78.731.982", "Gecz9RA8Fgx",21),
                    ("Gwyn", "Pardal", "gpardall@vistaprint.com", "60.957.945", "IpA7F2",22),
                    ("Rutter", "Kellough", "rkelloughm@artisteer.com", "03.020.226", "GCbCF89Hp3",23),
                    ("Pavia", "Graveston", "pgravestonn@toplist.cz", "72.821.342", "2B93HGORe",24),
                    ("Margareta", "Leacock", "mleacocko@home.pl", "28.169.340", "ZxPmYe2R",25),
                    ("Adrianna", "Pegg", "apeggp@disqus.com", "30.109.590", "oyDoVv",26),
                    ("Demetrius", "De Moreno", "ddemorenoq@zimbio.com", "53.278.926", "uDnUox",27),
                    ("Say", "Mulqueeny", "smulqueenyr@weebly.com", "25.137.093", "cxSFrtSaHTX",28),
                    ("Ferdinanda", "Maypother", "fmaypothers@geocities.com", "78.457.239", "tMvFHMA",29),
                    ("Charlene", "Vearncombe", "cvearncombet@hao123.com", "33.896.159", "J2bDAm",30)
         ]
        create_usuario(conn, usuario)