from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from interfas_BD import*
from datetime import date, time, datetime

numero_de_articulos= 6                  #numero maximo de articulos distintos permitidos

lista_comp=[]                           #lista para almacenar datos de  las compras del cliente
cantidadArticulo = 0                    #contador para el limite de articulos

class cliente(comunicacion):
    def __init__(self,ventana,cliente):
        comunicacion.__init__(self)
        self.ventana_cliente = ventana
        self.nombre_cliente_inicio = cliente

        self.ventana_cliente.title("Supermercado Tortuga --CLIENTE--")
        self.ventana_cliente.geometry("680x580")
        self.ventana_cliente.configure(bg="SkyBlue3")

        
        
        self.boton_cofirmar_compra = ttk.Button(self.ventana_cliente,text="COMPRAR",command=self.confirmar_compra).place(x=880,y=370,width=90,height=50)
        self.boton_cerrar_carrito= ttk.Button(self.ventana_cliente,text="<--",command=self.cerrar_mi_carrito).place(x=1100,y=400,width=90,height=60)
        
        self.frame_derecha_cliente= Frame(self.ventana_cliente, bg="light blue",width=680,height=580).pack(side=LEFT)
        self.boton_carrito = ttk.Button(self.frame_derecha_cliente,text="MI CARRITO",command=self.mi_carrito).place(x=580,y=20,width=90,height=90)

# -------------------------------------FRAME PARA COMPRAR POR DEFECTO-----------------------------------------#
        self.boton_comprar_frame = ttk.Button(self.ventana_cliente,text="COMBRAR",command=self.abrir_frame_comprar).place(x=10,y=400,width=90,height=38)
        self.boton_devolver_frame2 = ttk.Button(self.ventana_cliente,text="DEVOLVER PRODUCTO",command=self.abrir_frame2_devolver).place(x=150,y=400,width=130,height=38)

        self.frame_cliente = Frame(self.ventana_cliente,bg="cadet blue",width=500,height=100).place(x=10,y=430)

        self.etiqueta_propia= Label(self.ventana_cliente,bg="cadet blue",text="Creado por -- Mario Diaz -- CN4 1000ProgramadoresSalteños").place(x=10,y=560)
        self.etiqueta_titulo= Label(self.ventana_cliente,bg="light blue",text="SUPERMARK",font=("Arial",18)).place(x=10,y=10)
        self.etiqueta_micarrito= Label(self.ventana_cliente,bg="SkyBlue3",text="MI CARRITO DE COMPRAS",font=("Arial",18)).place(x=800,y=20)

        self.id_producto_comprar= Entry(self.ventana_cliente,bg="lightgrey",font=("Arial",12)).place(x=15,y=470,width=90,height=30)
        self.id_producto_comprar_etiqueta= Label(self.ventana_cliente,text="ID del producto a comprar:").place(x=12,y=440)
        
        self.cantidad_comprar= Entry(self.ventana_cliente,bg="lightgrey",font=("Arial",12)).place(x=240,y=470,width=90,height=30)
        self.cantidad_comprar_etiqueta= Label(self.ventana_cliente,text="cantidad:").place(x=240,y=440)

        self.boton_comprar= ttk.Button(self.ventana_cliente,text="Comprar")
        self.boton_comprar.pack()
        self.boton_comprar.place(x=400,y=470,width=90,height=50)

# -------------------------------------BUSCAR-----------------------------------------#
        self.lframe_buscar = LabelFrame(self.ventana_cliente, text="Buscar producto", bg="cadet blue")
        self.lframe_buscar.pack(padx=20, pady=20)
        self.lframe_buscar.place(x=20, y=90,width=530,height=50)

        self.nombre_buscar = Entry(self.lframe_buscar, bg="lightgrey", width=55)
        self.nombre_buscar.grid(row=0, column=1, columnspan=4)
        self.boton_buscar_fram4 = ttk.Button(self.lframe_buscar, text='Buscar',command=self.llenar_tabla_dato_cliente).grid(row=0, column=7)
        self.boton2_buscar_todo_fram4 = ttk.Button(self.lframe_buscar, text='Ver todo',command=self.llenar_tabla_dato_cliente_todo).grid(row=0, column=8)

# -------------------------------------TABLA BUSCAR-----------------------------------------#
        self.barra = ttk.Treeview(self.ventana_cliente)
        self.barra["columns"] = ('ID', "Nombre", "Marca","Precio", "Descripcion")
        self.barra.column('#0', width=0)
        self.barra.column('#1', anchor=CENTER, width=50)
        self.barra.column('#2', anchor=CENTER, width=120)
        self.barra.column('#3', anchor=CENTER, width=120)
        self.barra.column('#4', anchor=CENTER, width=60)
        self.barra.column('#5', anchor=CENTER, width=200)
        self.barra.place(x=0, y=150)

        self.barra.heading("#0", text="")
        self.barra.heading("#1", text="ID")
        self.barra.heading("#2", text="Nombre")
        self.barra.heading("#3", text="Marca")
        self.barra.heading("#4", text="Precio")
        self.barra.heading("#5", text="Descripcion")

        self.abrir_frame_comprar()

# -------------------------------------TABLA CLIENTE-----------------------------------------#       
        self.barra_carrito = ttk.Treeview(self.ventana_cliente)
        #self.barra_carrito.pack()
        
        self.barra_carrito["columns"] = ('ID', "Nombre", "Marca","Precio", "Descripcion","cantidad")
        self.barra_carrito.column('#0', width=0)
        self.barra_carrito.column('#1', anchor=CENTER, width=50)
        self.barra_carrito.column('#2', anchor=CENTER, width=100)
        self.barra_carrito.column('#3', anchor=CENTER, width=100)
        self.barra_carrito.column('#4', anchor=CENTER, width=70)
        self.barra_carrito.column('#5', anchor=CENTER, width=150)
        self.barra_carrito.column('#6', anchor=CENTER, width=50)

        self.barra_carrito.heading("#0", text="")
        self.barra_carrito.heading("#1", text="ID")
        self.barra_carrito.heading("#2", text="Nombre")
        self.barra_carrito.heading("#3", text="Marca")
        self.barra_carrito.heading("#4", text="Precio")
        self.barra_carrito.heading("#5", text="Descripcion")
        self.barra_carrito.heading("#6", text="cantidad")

        self.barra_carrito.place(x=680,y=100)
#=================================LLENAR TABLA CON PRODUCTO ESPECIFICO================================================#
    def llenar_tabla_dato_cliente(self):
        registros= self.barra.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra.delete(registro)

        buscar = self.nombre_buscar.get()                   #me trae todos los registros que estoy buscando en BD
        rows= super(cliente,self).buscar_producto(buscar)
        for row in rows:
            id = row[0]
            self.barra.insert("",END,id,text=id,values=row)

#=================================LLENAR TABLA CON TODOS LOS PRODUCTOS================================================#
    def llenar_tabla_dato_cliente_todo(self):
        registros= self.barra.get_children()                #limpia todos los datos que estan en la tabla
        for registro in registros:
            self.barra.delete(registro)

        rows= super(cliente,self).mostrar_dato_cliente()
        for row in rows:
            id = row[0]
            self.barra.insert("",END,id,text=id,values=row)

#-----------------------ABRIR FRAMES PARA COMPRAR-----------------------------------------#
    def abrir_frame_comprar(self):
        self.frame1 = Frame(self.ventana_cliente,bg="cadet blue",width=500,height=100).place(x=10,y=430)

        self.id_producto_comprar= Entry(self.ventana_cliente,bg="lightgrey",font=("Arial",12))
        self.id_producto_comprar.pack()
        self.id_producto_comprar.place(x=15,y=470,width=90,height=30)
        self.id_producto_comprar_etiqueta= Label(self.ventana_cliente,text="ID del producto a comprar:").place(x=12,y=440)
        
        self.cantidad_comprar= Entry(self.ventana_cliente,bg="lightgrey",font=("Arial",12))
        self.cantidad_comprar.place(x=240,y=470,width=90,height=30)
        #self.cantidad_comprar.pack()
        self.cantidad_comprar_etiqueta= Label(self.ventana_cliente,text="cantidad:").place(x=240,y=440)

        self.boton_comprar= ttk.Button(self.ventana_cliente,text="Comprar",command=self.enviar_compra).place(x=400,y=470,width=90,height=50)

#-----------------------ABRIR FRAMES PARA DEVOLVER-----------------------------------------#
    def abrir_frame2_devolver(self):
        self.frame2 = Frame(self.ventana_cliente,bg="red",width=500,height=100).place(x=10,y=430)

        self.id_producto_devolver= Entry(self.ventana_cliente,bg="lightgrey",font=("Arial",12))
        self.id_producto_devolver.pack()
        self.id_producto_devolver.place(x=15,y=470,width=90,height=30)
        self.id_producto_devolver_etiqueta= Label(self.ventana_cliente,text="ID del producto a devolver:").place(x=12,y=440)

        self.boton_devolver= ttk.Button(self.ventana_cliente,text="Devolver",command=self.devolver_compra).place(x=400,y=455,width=90,height=50)
        
#-----------------------COMPRAR PRODUCTO-----------------------------------------#
    def enviar_compra(self):
        global cantidadArticulo
        try:                                                              
            idProducto =int(self.id_producto_comprar.get())               #si se ingresa un valor distinto al id del producto si es un str ej
            try:                                                          #si el valor ingresado no es un numero muestra error
                cantidad =int(self.cantidad_comprar.get())
                #print(comprando)
            
                if cantidad > 0:
                    try:
                        if super(cliente,self).consultar_stock(idProducto)>=cantidad:        #consulta a la BD si hay stock para comprar
                            print("se puede comprar")

                            cantidadArticulo = cantidadArticulo +1
                            
                            if cantidadArticulo <= numero_de_articulos:                 #controla la cantidad de productos
                                self.llenar_micarrito(idProducto,cantidad)              # si hay stock y no excedo el limite de compra se puede comprar
                            else:                                                       #aqui arriba|| posible error si se pone 2 veces el mismo producto
                                messagebox.showinfo(message=f"solo se puede comprar {numero_de_articulos} articulos deistintos",title="Cantidad de articulos")
                                cantidadArticulo = cantidadArticulo - 1        
                        else:
                            messagebox.showinfo(message=f"Solo quedan  {super(cliente,self).consultar_stock(idProducto)}  productos",title="Stock insuficiente")
                    except:
                        messagebox.showerror(message="el id del articulo no esta en nuestra lista de productos",title="Articulo no encontrado")
                        cantidadArticulo = cantidadArticulo - 1      
                else:
                    messagebox.showerror(message="la cantidad minima de compra por articulo es de 1",title="Cantidad minima requerida")
            except:
                messagebox.showerror(message="el valor ingresado en cantidad no es un valor numerico",title="Cantidad no valida")
        except:
            messagebox.showerror(message="El id del articulo  no es un valor numerico",title="id articulo ingresado no valido")

#-----------------------DEVOLVER PRODUCTO----------------------FALTA OCULTAR LA ETIQUETA DEVOLVER-------------------#
    def devolver_compra(self):
        global cantidadArticulo
        try:                                                        #si el id del articulo a eliminar no esta en la lista de carrito
            id_producto_devolver= self.id_producto_devolver.get()   #muestra error

            self.barra_carrito.delete(id_producto_devolver)         #elimino el producto de la tabla carrito
            devolver=True

            print(lista_comp)

            while devolver:
                for i in range(len(lista_comp)):
                    id_tupla=lista_comp[i]                                   #obtengo la tuplas de la lista
                
                    if id_tupla[0] == int(id_producto_devolver):              #si el primer item de la tupla es == a id que quiero eliminar
                        
                        """self.etiqueta_item_eliminado= Label(self.ventana_cliente,text=f"se elimino el item:  {id_tupla[1]}",fg="red",font=("Arial",12))                            #almaceno la tupla a eliminar
                        self.etiqueta_item_eliminado.pack()
                        self.etiqueta_item_eliminado.place(x=150,y=50)      #funciona mas o menos
                        
                        self.etiqueta_item_comprado.pack(side="botom")"""

                        eliminar = id_tupla
                        devolver = False
                lista_comp.remove(eliminar)                             #elimino la tupla 
            print(lista_comp)
            if cantidadArticulo>0:
                cantidadArticulo = cantidadArticulo -1
            else:
                messagebox.showinfo(message="no hay articulos en el carrito",title="Carrito vacio")
        except:
            messagebox.showerror(message="El id del articulo  no se encuentra en el carrito",title="id articulo ingresado no valido")

#-----------------------ABRE VENTANA MI CARRITO DE PRODUCTO-----------------------------------------#
    def mi_carrito(self):
        self.ventana_cliente.geometry("1220x580")

#-----------------------CIERRA VENTANA MI CARRITO DE PRODUCTO-----------------------------------------#
    def cerrar_mi_carrito(self):
        self.ventana_cliente.geometry("680x580")

#-----------------------LLENAR TABLA DE MI CARRITO LLENO--------------FALTA OCULTAR LA ETIQUETA COMPRAR--------------------------#
    def llenar_micarrito(self,idProducto,cantidad):
        buscarid= idProducto
        row= super(cliente,self).buscar_producto_micarrito(buscarid)
        list_T=list(row)                #agrego a la tupla de la BD  la cantidad a comprar
        list_T.append(cantidad)
        tupla_row=tuple(list_T)
        
        lista_comp.append(tupla_row)    #lista con los datos comprados
                                        #print(lista_comp)
        id=tupla_row[0]
        self.barra_carrito.insert("",END,id,text=id,values=tupla_row)
                
#====================CONFIRMAR COMPRA CARRITO VENTANA TRAGETA CREDITO===============================================#
    def confirmar_compra(self):
        cliente_actual = self.nombre_cliente_inicio
        print(lista_comp)
        print(cliente_actual)
        self.ventana_confirmar_comp = Toplevel()
        self.ventana_confirmar_comp.title("CONFIRMAR COMPRA")
        self.ventana_confirmar_comp.geometry("300x230")
        #targeta(ventana_confirmar_comp)

        self.etiqueta_info = Label(self.ventana_confirmar_comp,text="Ingrese los datos de su targeta",font=("Arial",12)).place(x=20,y=0)
        self.etiqueta_nom_banco = Label(self.ventana_confirmar_comp,text="nombre de su banco:",font=("Arial",10)).place(x=0,y=30)
        self.entrada_nom_banco  = Entry(self.ventana_confirmar_comp,bg="lightgrey",font=("Arial",12))
        self.entrada_nom_banco.place(x=30,y=50)

        self.etiqueta_nom_titular = Label(self.ventana_confirmar_comp,text="nombre del titular :").place(x=0,y=80)
        self.entrada_nom_titular = Entry(self.ventana_confirmar_comp,bg="lightgrey",font=("Arial",12))
        self.entrada_nom_titular.place(x=30,y=100)

        self.etiqueta_fecha_cad = Label(self.ventana_confirmar_comp,text="fecha de caducidad de su targeta :").place(x=0,y=130)
        self.entrada_fecha_cad = Entry(self.ventana_confirmar_comp,bg="lightgrey",font=("Arial",12))
        self.entrada_fecha_cad.place(x=30,y=150)

        self.etiqueta_formato_fecha = Label(self.ventana_confirmar_comp,text="dd/mm/aaaa").place(x=200,y=150)

        self.boton_comprar_final = ttk.Button(self.ventana_confirmar_comp,text="Enviar",command=self.enviar_targeta).place(x=90,y=180,width=100,height=50)

#====================CONFIRMAR COMPRA CARRITO ENVIA DATOS PARA INCERTAR BD===========================================#
    def enviar_targeta(self):
        banco = self.entrada_nom_banco.get()
        titular=self.entrada_nom_titular.get()
        fecha =self.entrada_fecha_cad.get()

        self.ventana_confirmar_comp.destroy()
        
        datotargeta =(banco,titular,fecha)
        super(cliente,self).ingresar_dato_targetacredito(datotargeta) #envio una tupla con los datos de la targeta del cliente para incertar a la BD

        id_cliente = super(cliente,self).consultar_ID_usuario(self.nombre_cliente_inicio)  #envio el nom de usuario a la BD, me trae  el num de ID del cliente
        num_comprobante = super(cliente,self).consultar_ID_targetacredito()  #obtengo de la BD el ultimo ID del cliente que compro y obtengo el num de conprobante

        d = datetime.now()
        fecha_compra = d.strftime('%d/%m/%Y  %H:%M:%S')  #obtengo la fecha y hora de la compra

        dato_comprobante = (fecha_compra,num_comprobante,id_cliente)  

        super(cliente,self).ingresar_dato_comprobante(dato_comprobante)  #envio por una tupla los datos para llenar la tabla comprobante de la BD

        self.terminar_todo(num_comprobante)
        
#=============================ENVIAR DATOS PARA LLENAR TABLA DETALLES=============================#
    def terminar_todo(self,num_comprobante):
        lista_datos_para_detalle=[]
        #lista_cantidad_productos=[]            #para almacenar cantidad de productos y calcular el precio

        print(num_comprobante)
        for i in range(len(lista_comp)):
            prodtup=lista_comp[i]
            id_prod =prodtup[0]
            canti_comp= prodtup[5]
            
            
            #lista_cantidad_productos.append(canti_comp)  #almaceno en una lista la cantidad de productos comprados 

            #print(i)
            tup=(num_comprobante,id_prod,canti_comp)
            lista_datos_para_detalle.append(tup)
        print(lista_datos_para_detalle)
        super(cliente,self).ingresar_dato_detalle(lista_datos_para_detalle)

        self.enviar_stock_actualizado()                                 #llamo a la funcion encargada de calcular el stock par actualizar

#=============================CALCULAR EL STOCK FINAL=============================#
    def enviar_stock_actualizado(self):
        for i in range(len(lista_comp)):
            prodtup=lista_comp[i]
            id_prod =prodtup[0]                                         #me da el id del producto 
            canti_comp= prodtup[5]                                      #me da la cantidad de productos comprados
            traer_stock=super(cliente,self).consultar_stock(id_prod)    #resivo el stock del producto
            stock_calculado= traer_stock-canti_comp                     #resto al stock traido la cantidad comprada
            super(cliente,self).actualizar_stock(stock_calculado,id_prod)       #envio el stock calculado para actualizar BD

#========================================FIN DEL CODIGO=======================================================#



"""if __name__ == '__main__':
    ventana = Tk()
    aplicacion = cliente(ventana,"marloc")

    #ventana.geometry("680x580")
    ventana.mainloop()
    
        #self.etiqueta_item_comprado= Label(self.ventana_cliente,text=f"se agrego el item:  {tupla_row[1]}",fg="green",font=("Arial",12))
        #self.etiqueta_item_comprado.pack()
        #self.etiqueta_item_comprado.place(x=150,y=50)
        #self.etiqueta_item_comprado.pack()
        
        #self.etiqueta_item_comprado.place_forget()
    """