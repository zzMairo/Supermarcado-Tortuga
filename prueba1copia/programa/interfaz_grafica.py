from tkinter import *
from tkinter import ttk
from interfas_BD import*
#from consulta import*
from tkinter import messagebox

class administrador(comunicacion):
    def __init__(self, ventana):
        comunicacion.__init__(self)
        self.ventan = ventana


        self.ventan.title('Supermercado Tortuga --ADMIN--')
        self.ventan.configure(bg="SlateGray1")

        self.boton_verclientes= ttk.Button(self.ventan,text="VER CLIENTES",command=self.ver_clientes).place(x=10,y=10,width=100,height=30)

        self.etiqueta_propia= Label(self.ventan,bg="cadet blue",text="Creado por -- Mario Diaz -- CN4 1000ProgramadoresSalteños").place(x=10,y=580)

        self.frame1 = LabelFrame(
        self.ventan, text="nuevo producto", bg="SkyBlue3",font=("Arial",12))
        self.frame1.pack(padx=20, pady=20)
        self.frame1.place(x=820, y=10, height=210)

        self.etiqueta1 = Label(self.frame1, text="Nombre: ", bg="SkyBlue3")
        self.etiqueta1.grid(row=0, column=0)
        self.nombre = Entry(self.frame1, bg="lightgrey")
        self.nombre.grid(row=0, column=1)

        self.etiqueta2 = Label(self.frame1, text="Marca: ", bg="SkyBlue3")
        self.etiqueta2.grid(row=1, column=0)
        self.marca = Entry(self.frame1, bg="lightgrey")
        self.marca.grid(row=1, column=1)

        self.etiqueta3 = Label(
        self.frame1, text="Fecha de vencimiento: ", bg="SkyBlue3")
        self.etiqueta3.grid(row=2, column=0)
        self.fecha_venc = Entry(self.frame1, bg="lightgrey")
        self.fecha_venc.grid(row=2, column=1)

        self.etiqueta4 = Label(self.frame1, text="Precio: ", bg="SkyBlue3")
        self.etiqueta4.grid(row=3, column=0)
        self.precio = Entry(self.frame1, bg="lightgrey")
        self.precio.grid(row=3, column=1)

        self.etiqueta5 = Label(self.frame1, text="Stock: ", bg="SkyBlue3")
        self.etiqueta5.grid(row=4, column=0)
        self.stock = Entry(self.frame1, bg="lightgrey")
        self.stock.grid(row=4, column=1)

        self.etiqueta6 = Label(self.frame1, text="Descuento: ", bg="SkyBlue3")
        self.etiqueta6.grid(row=5, column=0)
        self.descuento = Entry(self.frame1, bg="lightgrey")
        self.descuento.grid(row=5, column=1)

        self.etiqueta7 = Label(self.frame1, text="Descripcion: ", bg="SkyBlue3")
        self.etiqueta7.grid(row=6, column=0)
        self.descripcion = Entry(self.frame1, bg="lightgrey")
        self.descripcion.grid(row=6, column=1)

        self.boton_frame1_cargar = ttk.Button(self.frame1, text='cargar', command=self.enviar_producto)
        self.boton_frame1_cargar.place(x=10, y=155, height=30)

        self.boton_frame1_limpiar = ttk.Button(self.frame1, text='Limpiar',command=self.limpiar_entrada_datos)
        self.boton_frame1_limpiar.place(x=100, y=155, height=30)

        # ------------------------------ACTUALIZAR----------------------------------#
        self.frame2 = LabelFrame(
        self.ventan, text="Actualizar producto", bg="SkyBlue3",font=("Arial",12))
        self.frame2.pack()
        self.frame2.place(x=820, y=250, height=230)

        self.etiqueta0 = Label(self.frame2, text="ingrese ID a modificar: ", bg="SkyBlue3")
        self.etiqueta0.grid(row=0, column=0)
        self.id_A = Entry(self.frame2, bg="lightgrey")
        self.id_A.grid(row=0, column=1)

        self.etiqueta1 = Label(self.frame2, text="Nombre: ", bg="SkyBlue3")
        self.etiqueta1.grid(row=1, column=0)
        self.nombre_A = Entry(self.frame2, bg="lightgrey")
        self.nombre_A.grid(row=1, column=1)

        self.etiqueta2 = Label(self.frame2, text="Marca: ", bg="SkyBlue3")
        self.etiqueta2.grid(row=2, column=0)
        self.marca_A = Entry(self.frame2, bg="lightgrey")
        self.marca_A.grid(row=2, column=1)

        self.etiqueta3 = Label(
        self.frame2, text="Fecha de vencimiento: ", bg="SkyBlue3")
        self.etiqueta3.grid(row=3, column=0)
        self.fecha_venc_A = Entry(self.frame2, bg="lightgrey")
        self.fecha_venc_A.grid(row=3, column=1)

        self.etiqueta4 = Label(self.frame2, text="Precio: ", bg="SkyBlue3")
        self.etiqueta4.grid(row=4, column=0)
        self.precio_A = Entry(self.frame2, bg="lightgrey")
        self.precio_A.grid(row=4, column=1)

        self.etiqueta5 = Label(self.frame2, text="Stock: ", bg="SkyBlue3")
        self.etiqueta5.grid(row=5, column=0)
        self.stock_A = Entry(self.frame2, bg="lightgrey")
        self.stock_A.grid(row=5, column=1)

        self.etiqueta6 = Label(self.frame2, text="Descuento: ", bg="SkyBlue3")
        self.etiqueta6.grid(row=6, column=0)
        self.descuento_A = Entry(self.frame2, bg="lightgrey")
        self.descuento_A.grid(row=6, column=1)

        self.etiqueta7 = Label(self.frame2, text="Descripcion: ", bg="SkyBlue3")
        self.etiqueta7.grid(row=7, column=0)
        self.descripcion_A = Entry(self.frame2, bg="lightgrey")
        self.descripcion_A.grid(row=7, column=1)

        self.boton_frame2_cargar = ttk.Button(self.frame2, text='Cargar',command=self.enviar_actualizacion)
        self.boton_frame2_cargar.place(x=10, y=175, height=30)

        self.boton_frame2_traer_dato = ttk.Button(self.frame2, text='Traer datos',command=self.traer_dato_actualizar)
        self.boton_frame2_traer_dato.place(x=90, y=175, height=30)



        # ------------------------------ELIMINAR----------------------------------#
        self.frame3 = LabelFrame(
        self.ventan, text="Eliminar producto", bg="SkyBlue3",font=("Arial",12))
        self.frame3.pack()
        self.frame3.place(x=820, y=490, width=260, height=80)

        self.etiqueta_eliminar = Label(self.frame3, text="ID del producto: ", bg="SkyBlue3")
        self.etiqueta_eliminar.grid(row=0, column=0)
        self.id_E = Entry(self.frame3, bg="lightgrey")#id_E === id de eliminar
        self.id_E.grid(row=0, column=1)

        self.boton_frame3 = ttk.Button(self.frame3, text='Eliminar', command=self.enviar_eliminacion)
        self.boton_frame3.place(x=90, y=25, height=30)

        # -------------------------------------LABEL BUSCAR PRODUCTO-----------------------------------------#
        self.frame4 = LabelFrame(self.ventan, text="Buscar producto", bg="SkyBlue3")#)
        self.frame4.pack(padx=20, pady=20)
        self.frame4.place(x=80, y=50,width=700,height=100)

        self.nombre_B = Entry(self.frame4, bg="lightgrey", width=80)
        self.nombre_B.grid(row=0, column=1, columnspan=4)
        self.boton_buscar_fram4 = ttk.Button(self.frame4, text='Buscar',command=self.llenar_tabla_dato_especifico).grid(row=0,column=7)#place(x=500,y=0,width=100,height=30)
        self.boton_buscartodo_fram4 = ttk.Button(self.frame4, text='Ver todo',command=self.llenar_tabla_dato_todo).grid(row=0,column=8)#place(x=500,y=50,width=30,height=20)

        #=======================================LABEL BUSCAR COMPRA POR NUMERO DE COMPRA=========================#
        self.frame5 = LabelFrame(self.ventan, text="Buscar compra del usuario por numero de compra", bg="SkyBlue3")#)
        self.frame5.pack()
        self.frame5.place(x=430, y=330,width=380,height=50)

        self.numero_compra_cliente = Entry(self.frame5, bg="lightgrey", width=20)
        self.numero_compra_cliente.grid(row=0, column=1, columnspan=4)
        self.boton_buscar_fram5 = ttk.Button(self.frame5, text='Buscar',command=self.llenar_tabla_productos_cliente).grid(row=0,column=7)#place(x=500,y=0,width=100,height=30)

        #=============================LABEL PARA ACTUALIZAR LISTA DE USUARIOS QUE COMPRARON=========================================================#
        self.lframe_usuario_compraron= LabelFrame(self.ventan,text="Usuarios que compraron",bg="SkyBlue3")
        self.lframe_usuario_compraron.pack()
        self.lframe_usuario_compraron.place(x=10, y=330,width=380,height=50)
        
        self.boton_actualizar_usuarios_compraron= ttk.Button(self.lframe_usuario_compraron,text="ACTUALIZAR",command=self.llenar_tabla_dato_cliente)
        self.boton_actualizar_usuarios_compraron.pack
        self.boton_actualizar_usuarios_compraron.grid(row=0,column=3)
        # -------------------------------------TABLA BUSCAR-----------------------------------------#
        self.barra = ttk.Treeview(self.ventan)
        self.barra["columns"] = ('ID', "Nombre", "Marca", "fecha de vencimiento","Precio", "Stock", "Descuento", "Descripcion")
        self.barra.column('#0', width=0)
        self.barra.column('#1', anchor=CENTER, width=20)
        self.barra.column('#2', anchor=CENTER, width=110)
        self.barra.column('#3', anchor=CENTER, width=110)
        self.barra.column('#4', anchor=CENTER, width=130)
        self.barra.column('#5', anchor=CENTER, width=80)
        self.barra.column('#6', anchor=CENTER, width=80)
        self.barra.column('#7', anchor=CENTER, width=80)
        self.barra.column('#8', anchor=CENTER, width=200)
        self.barra.place(x=0, y=100)

        self.barra.heading("#0", text="")
        self.barra.heading("#1", text="ID")
        self.barra.heading("#2", text="Nombre")
        self.barra.heading("#3", text="Marca")
        self.barra.heading("#4", text="Fecha de vencimiento")
        self.barra.heading("#5", text="Precio")
        self.barra.heading("#6", text="Stock")
        self.barra.heading("#7", text="Descuento")
        self.barra.heading("#8", text="Descripcion")

# -------------------------------------TABLA USUARIO QUE COMPRARON-----------------------------------------#
        self.barra_comprado = ttk.Treeview(self.ventan)
        self.barra_comprado["columns"] = ('Nro compra', "Fecha y Hora", "Nombre de usuario","Banco")
        self.barra_comprado.column('#0', width=0)
        self.barra_comprado.column('#1', anchor=CENTER, width=20)
        self.barra_comprado.column('#2', anchor=CENTER, width=90)
        self.barra_comprado.column('#3', anchor=CENTER, width=100)
        self.barra_comprado.column('#4', anchor=CENTER, width=100)

        self.barra_comprado.heading("#0", text="")
        self.barra_comprado.heading("#1", text="Nro compra")
        self.barra_comprado.heading("#2", text="Fecha")
        self.barra_comprado.heading("#3", text="Nombre de usuario")
        self.barra_comprado.heading("#4", text="Banco")

        self.barra_comprado.place(x=10, y=380,width=400,height=200)

# ============================TABLA LISTA DE COMPRA DE LOS USUARIOS ===================================#
        self.barra_carrito_comprado = ttk.Treeview(self.ventan)
        self.barra_carrito_comprado["columns"] = ('Nombre', "Marca", "precio","cantidad")
        self.barra_carrito_comprado.column('#0', width=0)
        self.barra_carrito_comprado.column('#1', anchor=CENTER, width=90)
        self.barra_carrito_comprado.column('#2', anchor=CENTER, width=90)
        self.barra_carrito_comprado.column('#3', anchor=CENTER, width=60)
        self.barra_carrito_comprado.column('#4', anchor=CENTER, width=60)

        self.barra_carrito_comprado.heading("#0", text="")
        self.barra_carrito_comprado.heading("#1", text="Nombre")
        self.barra_carrito_comprado.heading("#2", text="Marca")
        self.barra_carrito_comprado.heading("#3", text="precio")
        self.barra_carrito_comprado.heading("#4", text="cantidad")

        self.barra_carrito_comprado.place(x=430, y=380,width=380,height=200)

#=====================================LIMPIAR DATOS DE NUEVO PRODUCTO ===================================#
    def limpiar_entrada_datos(self):
        self.nombre.delete(0,"end")             #limpio lo que este escrito en los entry de ingresar nuevo producto
        self.marca.delete(0,"end")
        self.fecha_venc.delete(0,"end")
        self.precio.delete(0,"end")
        self.stock.delete(0,"end")
        self.descuento.delete(0,"end")
        self.descripcion.delete(0,"end")
    
#==================================LLENAR DATOS A ACTUaLIZAR===================================    
    def traer_dato_actualizar(self):
        tupla_dato_Actu=super(administrador,self).mostrar_datos_para_actualizar(self.id_A.get())

        self.nombre_A.delete(0,"end")               #elimino lo que tengan los entry antes de traer datos
        self.marca_A.delete(0,"end")
        self.fecha_venc_A.delete(0,"end")
        self.precio_A.delete(0,"end")
        self.stock_A.delete(0,"end")
        self.descuento_A.delete(0,"end")
        self.descripcion_A.delete(0,"end")

        self.nombre_A.insert(0,tupla_dato_Actu[1])          #inserto datos traidos de la BD e incerto en los entry 
        self.marca_A.insert(0,tupla_dato_Actu[2])
        self.fecha_venc_A.insert(0,tupla_dato_Actu[3])
        self.precio_A.insert(0,tupla_dato_Actu[4])
        self.stock_A.insert(0,tupla_dato_Actu[5])
        self.descuento_A.insert(0,tupla_dato_Actu[6])
        self.descripcion_A.insert(0,tupla_dato_Actu[7])

#=====================================LLENAR TABLA BUSCAR TODO DE PRODUCTOS ===================================#
    def llenar_tabla_dato_todo(self):
        registros= self.barra.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra.delete(registro)

        rows= super(administrador,self).mostrar_dato()
        for row in rows:
            id = row[0]
            self.barra.insert("",END,id,text=id,values=row)

#=====================================LLENAR TABLA BUSCAR PRODUCTO ESPECIFICO ===================================#
    def llenar_tabla_dato_especifico(self):
        registros= self.barra.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra.delete(registro)

        buscar = self.nombre_B.get()
        rows= super(administrador,self).buscar_producto_ADMIN(buscar)
        for row in rows:
            id = row[0]
            self.barra.insert("",END,id,text=id,values=row)

#============================LLENAR TABLA DE USUARIOS QUE COMPRARON COMPROBANTE ==================================#
    def llenar_tabla_dato_cliente(self):
        rows= super(administrador,self).consultar_dato_comprobante()
        for row in rows:
            id = row[0]
            self.barra_comprado.insert("",END,id,text=id,values=row)

#============================LLENAR TABLA DE PRODUCTOS QUE  LOS USUARIOS COMPRARON DETALLE =========================#
    def llenar_tabla_productos_cliente(self):
        registros= self.barra_carrito_comprado.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra_carrito_comprado.delete(registro)


        numero_de_compra = self.numero_compra_cliente.get()
        rows= super(administrador,self).consultar_dato_detalle(int(numero_de_compra))
        for row in rows:
            id = row[0]
            self.barra_carrito_comprado.insert("",END,id,text=id,values=row)
#-----------------------INCERTAR PRODUCTO BDD-----------------------------------------#
    def enviar_producto(self):
        producto_Nuevo = self.nombre.get(),self.marca.get(),self.fecha_venc.get(),self.precio.get(),self.stock.get(),self.descuento.get(),self.descripcion.get()
        super(administrador,self).incertar_producto(producto_Nuevo)
        print("PRODUCTO INCERTADO")
        self.limpiar_entrada_datos()

#-----------------------ACTUALIZAR PRODUCTO BDD-----------------------------------------#
    def enviar_actualizacion(self):
        producto_Actualizado = self.nombre_A.get(),self.marca_A.get(),self.fecha_venc_A.get(),self.precio_A.get(),self.stock_A.get(),self.descuento_A.get(),self.descripcion_A.get(),self.id_A.get()
        super(administrador,self).actualizar_producto(producto_Actualizado)
        print("PRODUCTO ACTUALIZADO")

        self.nombre_A.delete(0,"end")               #elimino lo que tengan los entry antes de traer datos
        self.marca_A.delete(0,"end")
        self.fecha_venc_A.delete(0,"end")
        self.precio_A.delete(0,"end")
        self.stock_A.delete(0,"end")
        self.descuento_A.delete(0,"end")
        self.descripcion_A.delete(0,"end")

#-----------------------ELIMINAR PRODUCTO BDD-----------------------------------------#
    def enviar_eliminacion(self):
        producto_Eliminado = self.id_E.get()
        super(administrador,self).eliminar_producto(producto_Eliminado)
        print("PRODUCTO ELIMINADO")

    def ver_clientes(self):
        self.ventana_clientes_admin=Toplevel()
        self.ventana_clientes_admin.geometry("1300x500")
        self.ventana_clientes_admin.title("clientes registrados")
        self.ventana_clientes_admin.config(bg="lightblue")

        # ============================TABLA LISTA DE COMPRA DE LOS USUARIOS ===================================#
        self.barra_clientes_registrados = ttk.Treeview(self.ventana_clientes_admin)
        self.barra_clientes_registrados["columns"] = ("id",'Nombre', "Apellido", "Usuario","Email","DNI","Tipo","Contraseña","Calle1","Calle2","Numero","Ruta","Km","Num_depa","Piso","Provincia","Localidad","Departamento")
        self.barra_clientes_registrados.column('#0', width=0)
        self.barra_clientes_registrados.column('#1', anchor=CENTER, width=30)
        self.barra_clientes_registrados.column('#2', anchor=CENTER, width=90)
        self.barra_clientes_registrados.column('#3', anchor=CENTER, width=60)
        self.barra_clientes_registrados.column('#4', anchor=CENTER, width=80)
        self.barra_clientes_registrados.column('#5', anchor=CENTER, width=100)
        self.barra_clientes_registrados.column('#6', anchor=CENTER, width=100)
        self.barra_clientes_registrados.column('#7', anchor=CENTER, width=60)
        self.barra_clientes_registrados.column('#8', anchor=CENTER, width=90)
        self.barra_clientes_registrados.column('#9', anchor=CENTER, width=90)
        self.barra_clientes_registrados.column('#10', anchor=CENTER, width=90)
        self.barra_clientes_registrados.column('#11', anchor=CENTER, width=60)
        self.barra_clientes_registrados.column('#12', anchor=CENTER, width=60)
        self.barra_clientes_registrados.column('#13', anchor=CENTER, width=60)
        self.barra_clientes_registrados.column('#14', anchor=CENTER, width=30)
        self.barra_clientes_registrados.column('#15', anchor=CENTER, width=30)
        self.barra_clientes_registrados.column('#16', anchor=CENTER, width=80)
        self.barra_clientes_registrados.column('#17', anchor=CENTER, width=80)
        self.barra_clientes_registrados.column('#18', anchor=CENTER, width=80)

        self.barra_clientes_registrados.heading("#0", text="")
        self.barra_clientes_registrados.heading("#1", text="id")
        self.barra_clientes_registrados.heading("#2", text="Nombre")
        self.barra_clientes_registrados.heading("#3", text="Apellido")
        self.barra_clientes_registrados.heading("#4", text="Usuario")
        self.barra_clientes_registrados.heading("#5", text="Email")
        self.barra_clientes_registrados.heading("#6", text="DNI")
        self.barra_clientes_registrados.heading("#7", text="Tipo")
        self.barra_clientes_registrados.heading("#8", text="Contraseña")
        self.barra_clientes_registrados.heading("#9", text="Calle1")
        self.barra_clientes_registrados.heading("#10", text="Calle2")
        self.barra_clientes_registrados.heading("#11", text="Numero")
        self.barra_clientes_registrados.heading("#12", text="Ruta")
        self.barra_clientes_registrados.heading("#13", text="Km")
        self.barra_clientes_registrados.heading("#14", text="Num_depa")
        self.barra_clientes_registrados.heading("#15", text="Piso")
        self.barra_clientes_registrados.heading("#16", text="Provincia")
        self.barra_clientes_registrados.heading("#17", text="Localidad")
        self.barra_clientes_registrados.heading("#18", text="Departamento")

        self.barra_clientes_registrados.place(x=0, y=0)

        
        registros= self.barra_clientes_registrados.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra_clientes_registrados.delete(registro)

        rows= super(administrador,self).consultar_todo_usuario()
        for row in rows:
            id = row[0]
            self.barra_clientes_registrados.insert("",END,id,text=id,values=row)

        self.etiqueta_info= Label(self.ventana_clientes_admin, text="Aqui puede seleccionar el ID de un usuario para cambiarlo a administrador",font=("Arial",12)).place(x=300,y=250)
        self.etiqueta_nombrar_admin= Label(self.ventana_clientes_admin, text="Ingrese el ID de Usuario:",font=("Arial",12)).place(x=480,y=310)
        self.etiqueta_enviar_admin =Entry(self.ventana_clientes_admin,font=("Arial",18))
        self.etiqueta_enviar_admin.place(x=660,y=300,width=50,height=50)#
        
        self.boton_enviar_admin= ttk.Button(self.ventana_clientes_admin,text="Cargar",command=self.enviar_ID_admin_nuevo).place(x=730,y=300,width=100,height=50)
    
    def enviar_ID_admin_nuevo(self):
        super(administrador,self).actualizar_tipo_usuario(self.etiqueta_enviar_admin.get())
        messagebox.showinfo(message="el usuario se cambio a Administrador",title="Registrar administrador")

"""if __name__ == '__main__':
    ventana = Tk()
    aplicacion = administrador(ventana)
    ventana.geometry("1100x600")
    ventana.mainloop()"""
