
import os

contactos=[]
contactos2=[]

class Contacto:
    def listado(self):
        print(f"Contactos: {contactos}")

        def modificar(self):
            contactos.remove(self.telefono)
            n=input("Nuevo Telefono: ")
            contactos.append(n) 
            contactos2.append(n) 
            print(f"Se ha modificado con exito {self.telefono} por {n}")
            contactos.remove(self.mail)
            nm=input("Nuevo Mail: ")
            contactos.append(nm) 
            contactos2.append(nm) 
            print(f"Se ha modificado con exito {self.mail} por {nm}")
            contactos.remove(self.address)
            na=input("Nuevo address: ")
            contactos.append(na) 
            contactos2.append(na) 
            print(f"Se ha modificado con exito {self.address} por {na}")
        def crearcontactos(self):
            self.nombre = input("Nombre: ")
            contactos.append(self.nombre)
            self.telefono = input("Telefono: ")
            contactos.append(self.telefono)
            self.mail = input("Mail: ")
            contactos.append(self.mail)
            self.address = input("Direcion: ")
            contactos.address(self.address)



c1 = Contacto()   

op = int(input("Opcion: \n, 1-Crear contacto\n 2-Listado\n 3-Buscar\n 4-Modificar telefono,mail o direccion\n 5-Salir"))
if op == 1:
    c1.crearcontactos()
if op == 2:
    listado()
if op == 3:
    print("No se")
if op == 4:
    c1.modificar()
if op == 5:
    SystemExit("Adios")





