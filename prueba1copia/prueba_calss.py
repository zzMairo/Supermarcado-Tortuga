#class usuario:
    #def insert_prod(self,nombre,marca):
     #self.__nombre = nombre
     #elf.__marca = marca
from datetime import datetime
class Persona():
    def __init__(self, nombre, apellido, dni, edad,fecha):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__edad=edad
        self.__fecha =fecha

    def __str__(self):
        cadena = "\n nombre:"+self.__nombre
        cadena += "\n apellido:"+self.__apellido
        cadena += "\n dni:"+ str(self.__dni)
        cadena += "\n edad:"+str(self.__edad)
        cadena += "\n fecha:"+ str(self.__fecha)
        return cadena

    def fechaString(self):
        date_string= datetime.strftime(self.__fecha,"%d/%m/%y")
        return date_string
        
    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,newfecha):
         self.__fecha = newfecha




fecha = datetime(2022,10,12)
print("*** Fecha creada con datatime ***")
print(fecha)
p1= Persona("Ballesteros","Cristian",12345632,30,fecha)
informacion= p1
print(informacion)
print("*** Fecha del objeto llamando al metodo fechaString de la clase persona***")
fechaCadena= p1.fechaString()
print(fechaCadena)


