from tkinter import *
from tkinter import ttk
from usuario_GUI import*
from interfaz_grafica import*
from interfas_BD import*
from tkinter import messagebox

class usuario(administrador,cliente):
    def __init__(self,ventana_us):
        comunicacion.__init__(self)
        self.ventana_usuario = ventana_us
        self.ventana_usuario.title("Supermark")
        self.ventana_usuario.configure(bg="lime green")
        #self.ventana_usuario.iconbitmap("carro.ico")
        
        self.frame_derecha= Frame(self.ventana_usuario, bg="dark green",width=300,height=400).pack(side=RIGHT)
        self.etiqueta_propia= Label(self.ventana_usuario,bg="lime green",text="Creado por -- Mario Diaz -- CN4 1000ProgramadoresSalteños").place(x=10,y=380)

        #===============================INICIO DE SECION CUADRRO DE ICONOS DERECHA===================================#
        self.lframe_inicio = LabelFrame(self.frame_derecha, text="", bg="forest green",font=("Arial",12))
        self.lframe_inicio.place(x=475, y=100, height=200,width=250)

        self.img_us = PhotoImage(file=r"C:\Users\md418\Documents\unsa mario\python curso\PYTHON EJ\prueba1copia\imagenes\usuario.gif")
        self.img_usuario_chico= Label(self.lframe_inicio,image=self.img_us,bd=0, bg="forest green").place(x=10,y=30)

        self.img_can = PhotoImage(file=r"C:\Users\md418\Documents\unsa mario\python curso\PYTHON EJ\prueba1copia\imagenes\candado.gif")
        self.img_candado= Label(self.lframe_inicio,image=self.img_can,bd=0, bg="forest green").place(x=10,y=110)

        self.titulo_login = Label(self.frame_derecha, text="INICIO DE SESION ", font=("Arial",18),bg="dark green",fg="snow2")
        self.titulo_login.place(x=490,y=50)
        
        self.nombre = Entry(self.lframe_inicio, bg="lightgrey",font=("Arial",12))
        self.nombre.place(x=60,y=40,relwidth = 0.6,relheight = 0.15,)

        self.contraseña = Entry(self.lframe_inicio, bg="lightgrey",font=("Arial",12))
        self.contraseña.place(x=60,y=120,relwidth = 0.6,relheight = 0.15,)

        
#===============================INICIO DE SECION CUADRRO DE IZQUIERDA===================================#
        
        self.boton2= ttk.Button(self.lframe_inicio,text="Entrar",command=self.iniciar_sesion).place(x=80,y=160,width=100,height=30)

        self.titulo_bienvenido = Label(self.ventana_usuario, text="¡BIENVENID@! ", font=("Arial",22),bg="lime green")
        self.titulo_bienvenido.place(x=200,y=0)#Barlow Condensed Light Algerian
        self.titulo_bienvenido2 = Label(self.ventana_usuario, text="Nos alegramos", font=("Barlow Condensed",16),bg="lime green")
        self.titulo_bienvenido2.place(x=250,y=40)
        self.titulo_bienvenido3 = Label(self.ventana_usuario, text="de volver a verte", font=("Barlow Condensed",16),bg="lime green")
        self.titulo_bienvenido3.place(x=250,y=70)
        
        self.img_intro = PhotoImage(file=r"C:\Users\md418\Documents\unsa mario\python curso\PYTHON EJ\prueba1copia\imagenes\mario_tortuga_A-removebg-preview.gif")
        self.img_intro_tortuga= Label(self.ventana_usuario,image=self.img_intro,bd=0,bg="lime green").place(x=0,y=50)

        
        self.boton3_registrarce = ttk.Button(self.frame_derecha,text="Registrarse",command=self.registrarse).place(x=560,y=340,width=100,height=30)


#===============================INICIAR SECION BD===================================#
    def iniciar_sesion(self):
        nom_usuario = self.nombre.get()
        usuario_contra = self.contraseña.get()
        
        row_lista = super(usuario,self).consultar_usuario(nom_usuario,usuario_contra)
        
      

        if len(row_lista) != 0:
            print("se encontro")
            row_tupla = row_lista[0]
            if row_tupla[0] == 'admin':
                self.ventana_usuario.destroy()
                ventana = Tk()
                administrador(ventana)
                ventana.geometry("1100x600")
                

            elif row_tupla[0] == 'cliente':
                self.ventana_usuario.destroy()
                ventana_cliente = Tk()
                cliente(ventana_cliente,nom_usuario)
                #ventana_cliente.geometry("800x500")
                
        else:
            messagebox.showinfo(message=f"contraseña o usuario incorrecto",title="Inicio de sesion")

    def registrarse(self):
        self.ventana_registro= Toplevel()
        self.ventana_registro.geometry("300x450")
        self.ventana_registro.title("REGISTRARSE")
        self.ventana_registro.config(bg="lime green")

        self.frame_derecha_reegistro= Frame(self.ventana_registro,bg="dark green",width=300,height=450).pack(side=RIGHT)

        self.etiqueta_nom_reg = Label(self.ventana_registro,text="Nombre: ",font=("Arial",12))
        self.etiqueta_nom_reg.pack()
        self.etiqueta_nom_reg.place(x=10,y=25)

        self.entrada_nom_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_nom_reg.place(x=20,y=50)

        self.etiqueta_apell_reg = Label(self.ventana_registro,text="Apellido: ",font=("Arial",12))
        self.etiqueta_apell_reg.pack()
        self.etiqueta_apell_reg.place(x=10,y=85)

        self.entrada_apell_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_apell_reg.place(x=20,y=110)

        self.etiqueta_nomusuar_reg = Label(self.ventana_registro,text="Nombre de usuario: ",font=("Arial",12))
        self.etiqueta_nomusuar_reg.pack()
        self.etiqueta_nomusuar_reg.place(x=10,y=145)

        self.entrada_nomusuar_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_nomusuar_reg.place(x=20,y=170)

        self.etiqueta_email_reg = Label(self.ventana_registro,text="Email: ",font=("Arial",12))
        self.etiqueta_email_reg.pack()
        self.etiqueta_email_reg.place(x=10,y=205)

        self.entrada_email_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_email_reg.place(x=20,y=230)

        self.etiqueta_dni_reg = Label(self.ventana_registro,text="DNI: ",font=("Arial",12))
        self.etiqueta_dni_reg.pack()
        self.etiqueta_dni_reg.place(x=10,y=265)

        self.entrada_dni_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_dni_reg.place(x=20,y=290)

        self.etiqueta_contra_reg = Label(self.ventana_registro,text="Contraseña: ",font=("Arial",12))
        self.etiqueta_contra_reg.pack()
        self.etiqueta_contra_reg.place(x=10,y=325)

        self.entrada_contra_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_contra_reg.place(x=20,y=350)

        self.boton_pasar_ventana_reg = ttk.Button(self.ventana_registro,text="-->",command=self.registrarse_segunda_ventana)
        self.boton_pasar_ventana_reg .place(x=220,y=310,width=70,height=50)
        
#=========================================SEGUNDA VENTANA=========================================================================
        self.etiqueta_calle1_reg = Label(self.ventana_registro,text="Calle 1: ",font=("Arial",12))
        self.etiqueta_calle1_reg.pack()
        self.etiqueta_calle1_reg.place(x=310,y=25)

        self.entrada_calle1_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_calle1_reg.place(x=320,y=50)

        self.etiqueta_calle2_reg = Label(self.ventana_registro,text="Calle 2: ",font=("Arial",12))
        self.etiqueta_calle2_reg.pack()
        self.etiqueta_calle2_reg.place(x=310,y=85)

        self.entrada_calle2_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_calle2_reg.place(x=320,y=110)

        self.etiqueta_numero_reg = Label(self.ventana_registro,text="Numero: ",font=("Arial",12))
        self.etiqueta_numero_reg.pack()
        self.etiqueta_numero_reg.place(x=310,y=145)

        self.entrada_numero_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_numero_reg.place(x=320,y=170)

        self.etiqueta_ruta_reg = Label(self.ventana_registro,text="Ruta: ",font=("Arial",12))
        self.etiqueta_ruta_reg.pack()
        self.etiqueta_ruta_reg.place(x=310,y=205)

        self.entrada_ruta_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_ruta_reg.place(x=320,y=230)

        self.etiqueta_km_reg = Label(self.ventana_registro,text="Km: ",font=("Arial",12))
        self.etiqueta_km_reg.pack()
        self.etiqueta_km_reg.place(x=310,y=265)

        self.entrada_km_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_km_reg.place(x=320,y=290)

        self.etiqueta_nem_dapa_reg = Label(self.ventana_registro,text="Numero de departamento: ",font=("Arial",12))
        self.etiqueta_nem_dapa_reg.pack()
        self.etiqueta_nem_dapa_reg.place(x=310,y=325)

        self.entrada_num_depa_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_num_depa_reg.place(x=320,y=350)

        self.etiqueta_piso_reg = Label(self.ventana_registro,text="Piso: ",font=("Arial",12))
        self.etiqueta_piso_reg.pack()
        self.etiqueta_piso_reg.place(x=310,y=385)

        self.entrada_piso_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_piso_reg.place(x=320,y=410)

        self.boton_pasar_ventana2_reg = ttk.Button(self.ventana_registro,text="-->",command=self.registrarse_tercera_ventana)
        self.boton_pasar_ventana2_reg.place(x=520,y=310,width=70,height=50)
        
#==========================================TERCERA VENTANA REGISTARO=================================================
        self.etiqueta_prov_reg = Label(self.ventana_registro,text="Provincia: ",font=("Arial",12))
        self.etiqueta_prov_reg.pack()
        self.etiqueta_prov_reg.place(x=610,y=25)

        self.entrada_prov_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_prov_reg.place(x=620,y=50)

        self.etiqueta_localidad_reg = Label(self.ventana_registro,text="Localidad: ",font=("Arial",12))
        self.etiqueta_localidad_reg.pack()
        self.etiqueta_localidad_reg.place(x=610,y=85)

        self.entrada_localidad_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_localidad_reg.place(x=620,y=110)

        self.etiqueta_depa_reg = Label(self.ventana_registro,text="Departamento: ",font=("Arial",12))
        self.etiqueta_depa_reg.pack()
        self.etiqueta_depa_reg.place(x=610,y=145)

        self.entrada_depa_reg = Entry(self.ventana_registro, bg="lightgrey",font=("Arial",12))
        self.entrada_depa_reg.place(x=620,y=170)

        self.boton_confirmar_registro=ttk.Button(self.ventana_registro,text="Confirmar",command=self.enviar_dato_registro).place(x=720,y=310,width=70,height=50)

    def registrarse_segunda_ventana(self):
        if super(usuario,self).consultar_usuario_registro(self.entrada_nomusuar_reg.get()):
            if super(usuario,self).consultar_contraseña_registro(self.entrada_contra_reg.get()):
                self.ventana_registro.geometry("600x450")
                self.boton_pasar_ventana_reg.place_forget()
                self.entrada_nomusuar_reg.config(state="disabled")
                self.entrada_contra_reg.config(state="disabled")
                global ultimo_ID
                ultimo_ID=super(usuario,self).consultar_ultimo_ID_usuario()
                
                self.tupla_dato_usuarios=(self.entrada_nom_reg.get(),self.entrada_apell_reg.get(),self.entrada_nomusuar_reg.get(),self.entrada_email_reg.get(),self.entrada_dni_reg.get(),"cliente",self.entrada_contra_reg.get(),int(ultimo_ID)+1)
                
            else:
                messagebox.showerror(message="ingrese otra contraseña",title="Contraseña no valida")
        else:
            messagebox.showerror(message="El nombre de usuario ya esta ocupado",title="Usuario ingresado no valido")
        
    def registrarse_tercera_ventana(self):
            self.ventana_registro.geometry("900x450")
            self.boton_pasar_ventana2_reg.place_forget()
            self.tupla_dato_domicillo=(self.entrada_calle1_reg.get(),self.entrada_calle2_reg.get(),self.entrada_numero_reg.get(),self.entrada_ruta_reg.get(),self.entrada_km_reg.get(),self.entrada_num_depa_reg.get(),self.entrada_piso_reg.get(),int(ultimo_ID)+1)
    
    def enviar_dato_registro(self):
        self.tupla_dato_ciudad=(self.entrada_prov_reg.get(),self.entrada_localidad_reg.get(),self.entrada_depa_reg.get())
        
        super(usuario,self).ingresar_dato_usuarios(self.tupla_dato_usuarios)
        super(usuario,self).ingresar_dato_domicillo(self.tupla_dato_domicillo)
        super(usuario,self).ingresar_dato_ciudad(self.tupla_dato_ciudad)

        messagebox.showinfo(message="Usuario registrado",title="Registro exitoso")
        self.ventana_registro.destroy()

if __name__ == '__main__':
    ventana_usuario = Tk()
    aplicacion = usuario(ventana_usuario)
    ventana_usuario.geometry("750x400")
    ventana_usuario.resizable(False,False)
    ventana_usuario.mainloop()