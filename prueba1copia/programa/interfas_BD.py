import sqlite3
from sqlite3 import Error
#from incert_usuari_BDD import*
#from consulta import*
#from datetime import date, time, datetime


class comunicacion():
    def __init__(self):
        self.conexion = self.conectar()
        
#-----------------------CONECTAR BD-----------------------------------------#
    def conectar(self):
        conn = None
        try:
            conn = sqlite3.connect("Supermarker.db")
        except Error as e:
            print(e)
        return conn
#-----------------------MOSTRAR PRODUCTOS PARA ADMIN DE BD--------------USAR ADMIN---------------------------#
    def mostrar_dato(self):     
        cursor = self.conexion.cursor()
        cursor.execute("SELECT*FROM productos")
        row = cursor.fetchall()
        return row
#-----------------------MOSTRAR TODOS LOS PRODUCTOS PARA EL CLIENTE DE BD------------USAR CLIENTE-----------------------------#
    def mostrar_dato_cliente(self):        
        cursor = self.conexion.cursor()
        cursor.execute("SELECT id_producto, nombre, marca, precio, descripcion FROM productos")#precio
        row = cursor.fetchall()
        return row

#-----------------------CONSULTA SI FUNCIONA EL ENLACE DE LA CLASE -----------------------------------------#
    def hola(self):
        print("HOLA MUNDO")
#-----------------------INCERTAR PRODUCTO EN BD-----------------------------------------#
    def incertar_producto(self,producto):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO productos(nombre,marca,fecha_vencimiento,precio,stock,descuento,descripcion)
              VALUES(?,?,?,?,?,?,?) '''
        cursor.execute(sql,producto)
        self.conexion.commit()
        #self.conexion.close()

#-----------------------ACTUALIZAR PRODUCTO EN BD-----------------------------------------#
    def actualizar_producto(self,producto):
        cursor = self.conexion.cursor()
        sql = ''' UPDATE productos SET nombre=?, marca=?, fecha_vencimiento=?, precio=? ,stock=?, descuento=?, descripcion=? WHERE id_producto = ?;'''
        cursor.execute(sql,producto)
        self.conexion.commit()
        #self.conexion.close()

#-----------------------ACTUALIZAR STOCK EN BD-----------------------------------------#
    def actualizar_stock(self,stock,id_producto):
        cursor = self.conexion.cursor()
        sql = f"""UPDATE productos SET stock={stock} WHERE id_producto={id_producto}"""
        cursor.execute(sql)
        self.conexion.commit()

#-----------------------ELIMINAR PRODUCTO EN BDD-----------------------------------------#
    def eliminar_producto(self,product):
        cursor = self.conexion.cursor()
        sql = f' DELETE FROM productos WHERE id_producto={product};'
        cursor.execute(sql)
        self.conexion.commit()
        #self.conexion.close()

#-----------------------CONTROL DE STOCK DE PRODUCTOS EN BDD-----------------------------------------#
    def consultar_stock(self,id_producto):
        cursor = self.conexion.cursor()
        sql = f'SELECT stock FROM productos WHERE id_producto ={id_producto}'
        cursor.execute(sql)
        row = cursor.fetchall()
        stockTupla=row[0]
        stock =stockTupla[0]
        return stock

#-----------------------CONSULTAR DESCUENTO DE LOS PRODUCTOS EN BDD----------------NO SE USA -------------------------#
    def consultar_descuento(self,id_producto):
        cursor = self.conexion.cursor()
        sql = f'SELECT descuento FROM productos WHERE id_producto ={id_producto}'
        cursor.execute(sql)
        row = cursor.fetchall()
        descuentoTupla=row[0]
        descuento =descuentoTupla[0]
        return descuento

#-----------------------BUSCAR PRODUCTOs ESPESIFICO CLIENTE EN BDD-----------------------------------------#
    def buscar_producto(self,buscar):
        cursor = self.conexion.cursor()
        sql = f"SELECT id_producto, nombre, marca, precio, descripcion FROM productos WHERE nombre LIKE'%{buscar}%';"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
    
#-----------------------BUSCAR PRODUCTOs ESPESIFICO ADMIN EN BDD-----------------------------------------#
    def buscar_producto_ADMIN(self,buscar):
        cursor = self.conexion.cursor()
        sql = f"SELECT id_producto, nombre, marca, fecha_vencimiento, precio, stock, descuento, descripcion FROM productos WHERE nombre LIKE'%{buscar}%';"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

#-----------------------BUSCAR UN PRODUCTO ESPESIFICO PARA MI CARRITO EN BDD-----------------------------------------#
    def buscar_producto_micarrito(self,id_producto):
        cursor = self.conexion.cursor()
        sql = f'SELECT id_producto, nombre, marca, precio, descripcion FROM productos WHERE id_producto ={id_producto}'
        cursor.execute(sql)
        rows = cursor.fetchall()
        tupla1 =rows[0]
        return tupla1

#-----------------------REGISTRAR USUARIO BD-----------------------------------NO USAR DE MOMENTO-------------------------------#
    def incertar_usuario(self,usuario):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO usuarios(nombre,apellido,email,dni,contraseña,id_domicillo)
              VALUES(?,?,?,?,?,?) '''
        cursor.execute(sql,usuario)
        self.conexion.commit()
        #self.conexion.close()

#-----------------------INICIO DE SECION USUARIO BD-----------------------------------------#
    def consultar_usuario(self,usuario,contraseña):
        cursor = self.conexion.cursor()
        sql = f"SELECT tipo FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

#-----------------------CONSULTAR TODO  DE  USUARIO BD===============================================#
    def consultar_todo_usuario(self):
        cursor = self.conexion.cursor()
        #print(cursor)
        sql = f"""SELECT u.id_usuario, u.nombre, u.apellido, u.usuario, u.email, u.dni, u.tipo, u.contraseña,  d.calle1, d.calle2, d.numero, d.ruta, d.km, d.num_depa, d.piso, c.provincia, c.localidad, c.departamento                  

                FROM usuarios AS u,  domicillo AS d,   ciudad AS c 

                WHERE u.id_domicillo = d.id_domicillo AND d.id_ciudad=c.id_ciudad"""
        cursor.execute(sql)
        rows = cursor.fetchall()
        #print(rows)
        return rows
#-----------------------INGRESAR DATOS DEL USUARIO A TABLA COMPROBANTE BD-----------------------------------------#
    def ingresar_dato_comprobante(self,datocomprobante):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO comprobante (fecha, id_targetacredito, id_usuario)
              VALUES(?,?,?) '''
        cursor.execute(sql,datocomprobante)
        self.conexion.commit()

#-----------------------INGRESAR DATOS DEL USUARIO A TABLA DETALLE BD-----------------------------------------#
    def ingresar_dato_detalle(self,datodetalle):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO detalles (id_comprobante, id_producto, cantidad)
              VALUES(?,?,?) '''
        cursor.executemany(sql,datodetalle)
        self.conexion.commit()

#-----------------------INGRESAR DATOS DEL USUARIO A TABLA TARGETACREDITO BD-----------------------------------------#
    def ingresar_dato_targetacredito(self,datotargeta):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO targetacredito (banco, titular, fecha_caducidad)
              VALUES(?,?,?) '''
        cursor.execute(sql,datotargeta)
        self.conexion.commit()

#===============================INGRESAR DATO DELUSUARIO A TABLA USUARIOS===================================#
    def ingresar_dato_usuarios(self,datousuario):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO usuarios(nombre,apellido,usuario, email,dni,tipo,contraseña, id_domicillo)
              VALUES(?,?,?,?,?,?,?,?) '''
        cursor.execute(sql,datousuario)
        self.conexion.commit()

#===============================INGRESAR DATO DELUSUARIO A TABLA DOMICILLO===================================#
    def ingresar_dato_domicillo(self,datodomicillo):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO domicillo(calle1, calle2, numero, ruta, km, num_depa, piso, id_ciudad)
              VALUES(?,?,?,?,?,?,?,?) '''
        cursor.execute(sql,datodomicillo)
        self.conexion.commit()

#===============================INGRESAR DATO DELUSUARIO A TABLA CIUDAD===================================#
    def ingresar_dato_ciudad(self,datociudad):
        cursor = self.conexion.cursor()
        sql = ''' INSERT INTO ciudad(provincia, localidad, departamento)
              VALUES(?,?,?) '''
        cursor.execute(sql,datociudad)
        self.conexion.commit()

#=========================CONSULTAR TODO  DE  TABLA DETALLE BD=====================NO SE USA SOLO PARA VER DATOS DE DETALLE=======#
    def consultar_todo_detalle(self):
        cursor = self.conexion.cursor()
        #print(cursor)
        sql = f"""SELECT d.id_comprobante, c.fecha,t.banco, t.titular,t.fecha_caducidad, u.nombre,u.apellido,p.nombre,p.marca,d.cantidad                

                FROM detalles AS d,  comprobante AS c,   targetacredito AS t, productos AS p, usuarios AS u

                WHERE d.id_comprobante = c.id_comprobante AND c.id_targetacredito = t.id_targetacredito 
                        AND c.id_usuario = u.id_usuario   AND d.id_producto = p.id_producto
                        
                """
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)

#=============================CONSULTA ESPECIFICA DE TABLA COMPROBANTE BD==========================================#
    def consultar_dato_comprobante(self):
        cursor = self.conexion.cursor()
        sql = f"""SELECT c.id_comprobante, c.fecha, u.usuario, t.banco
                    FROM comprobante AS c, targetacredito AS t, usuarios AS u
                    WHERE c.id_targetacredito = t.id_targetacredito AND c.id_usuario = u.id_usuario
                """
        cursor.execute(sql)
        rows = cursor.fetchall()
        #print(rows)
        return rows

#=============================CONSULTA ESPECIFICA DE TABLA DETALLE BD==========================================#
    def consultar_dato_detalle(self,numero_compra):
        cursor = self.conexion.cursor()
        sql = f"""SELECT p.nombre, p.marca, p.precio, d.cantidad

                    FROM detalles AS d, productos AS p

                    WHERE d.id_producto = p.id_producto AND id_comprobante ={numero_compra}
                """
        cursor.execute(sql)
        rows = cursor.fetchall()
        #print(rows)
        return rows

#=============================CONSULTA ID USUARIO PASNDOLE EL NOMBRE DE USUARIO=============================#
    def consultar_ID_usuario(self,usuario):
        cursor = self.conexion.cursor()
        sql = f"SELECT id_usuario FROM usuarios WHERE usuario='{usuario}'"
        cursor.execute(sql)
        rows = cursor.fetchone()
        row = rows[0]
        print(row)
        return row

#================================CONSULTAR  EL ULTIMO ID_TRAGETACREDITO QUE INGRESO====================#
    def consultar_ID_targetacredito(self):
        cursor = self.conexion.cursor()
        sql = f"SELECT id_targetacredito FROM targetacredito  ORDER BY id_targetacredito DESC;"
        cursor.execute(sql)
        rows = cursor.fetchone()
        row = rows[0]
        return row

#================================CONSULTAR  NOMBRE USUARIO QUE INGRESO DEL REGISTRO EN BD====================#
    def consultar_usuario_registro(self,usuario):
        cursor = self.conexion.cursor()
        sql = f"SELECT usuario FROM usuarios WHERE usuario='{usuario}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows)==0:
            return True
        else:
            return False

#================================CONSULTAR CONTRASEÑA QUE INGRESO DEL REGISTRO EN BD====================#
    def consultar_contraseña_registro(self,contra):
        cursor = self.conexion.cursor()
        sql = f"SELECT contraseña FROM usuarios WHERE contraseña='{contra}'"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows)==0:
            return True
        else:
            return False

#=============================CONSULTA ULTIMO ID USUARIO PARA REGISTRO=============================#
    def consultar_ultimo_ID_usuario(self):
        cursor = self.conexion.cursor()
        sql = f"SELECT id_usuario FROM usuarios ORDER BY id_usuario DESC;"
        cursor.execute(sql)
        rows = cursor.fetchone()
        row = rows[0]
        #print(row)
        return row

#=============================ACTUALIZAR TIPO DE USUARIO=============================#
    def actualizar_tipo_usuario(self,idusuario):
        cursor = self.conexion.cursor()
        sql = f''' UPDATE usuarios SET tipo='Admin' WHERE id_usuario = {idusuario}'''
        cursor.execute(sql)
        self.conexion.commit()

#=============================BUSCAR DATOS PARA ACTUALIZAR POR ID=============================#
    def mostrar_datos_para_actualizar(self,idproducto):
        cursor = self.conexion.cursor()
        cursor.execute(f"SELECT*FROM productos WHERE id_producto={idproducto}")
        row = cursor.fetchone()
        return row


"""
us1 = comunicacion()
us1.mostrar_datos_para_actualizar(1)

us1 = comunicacion()
us1.consultar_domicillo()
        

us1.consultar_ultimo_ID_usuario()


us1.consultar_usuario_registro("Lystub")
us1.consultar_contraseña_registro("JhfMs")


us1 = comunicacion()
us1.consultar_descuento(61)

us1 = comunicacion()
us1.consultar_usuario("ma","dad")


us1 = comunicacion()
d=us1.consultar_dato_detalle(4)
print(d)

producto = [(1,"Chicken Half","laferre","1/7/2022",117,10,0,"pollo cosinado 1.5kg sin guarnicion",2),
                    (23,"Alcaparras","campo arta","7/6/2022",275,65,0,"alcaparras encurtidas baja calorias",33),
                    (3,"Rape - Fresco","sant bell","5/15/2022",268,11,0,"pescado fresco 1kg",4),
                    (4,"Vino - Tinto", "Harrow Estates","16/4/2022",175,103,0,"vino tinto 1lt",43),
                    (23,"Chalotes","zaparra","11/3/2022",294,102,0,"challote bolsa de 1kg",2)]
u=25
lis=[]
for i in range(len(producto)):
    prodtup=producto[i]
    id_prod =prodtup[0]
    canti_comp= prodtup[8]

    print(i)
    tup=(u,id_prod,canti_comp)
    lis.append(tup)
print(lis)
"""
"""
d = datetime.now()
print(d.strftime('%d/%m/%Y  %H:%M:%S'))

us1 = comunicacion()
us1.consultar_ID_targetacredito()

us1 = comunicacion()
us1.consultar_ID_usuario("Lystub")

    
us1 = comunicacion()
us1.consultar_dato_comprobante()

us1 = comunicacion()
us1.consultar_todo_detalle()

d.id_comprobante,d.id_producto,d.cantidad,c.*,t.*,p.nombre,p.marca

us1 = comunicacion()
dato=   [(1,2,5),
         (1,4,4),
         (1,21,2)    
       ]
us1.ingresar_dato_detalle(dato)



dato =("20/5/2022",1,3)
us1.ingresar_dato_comprobante(dato)



dato=("Rio","Ly","20/5/2022")
us1.ingresar_dato_targetacredito(dato)


us1 = comunicacion()
us1.consultar_domicillo()

ad ="Lystub"
print(us1.consultar_usuario(ad,"JhfMUs"))

q=us1.consultar_stock(8,90)
print(q)"""
"""buscar = "pan"
us1.buscar_producto(buscar)"""


"""us1 = comunicacion()
print(us1)
#us1.creando_tablas()
#main()
hh = us1.mostrar_dato()
print(hh)
consul()
us1.incertar_usuario(input("ingrese nombre:"),input("ingrese apellido: "),input("ingrese email:"),input("ingrese dni: "),input("ingrese contraseña: "),input("ingrese id_domicillo: "))
print(hh)"""
