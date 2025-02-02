import sqlite3
"""-------------------------------------------------------------------------------------------------------------------------"""

'''
miConexion = sqlite3.connect("Peluqueria")
miCursor = miConexion.cursor()
miCursor.execute("CREATE TABLE PERROS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PERRO VARCHAR(30) UNIQUE, DUEÑO VARCHAR(30), DOMICILIO VARCHAR (30), TELEFONO INTEGER(15), MOTIVO_DE_VISITA INTEGER(3))")
miConexion.commit()
miConexion.close()
'''

"""-------------------------------------------------------------------------------------------------------------------------"""
class ProgramaPrincipal:
    
    def menu(self):
        while True:
            print("\n****Menu de opciones Peluqueria Canina****")
            print("1- Cargar perro")
            print("2- Modificar datos de un perro")
            print("3- Borrar un perro")
            print("4-Cargar visita")
            print("5-Mostrar lista completa")   
            print("0- Salir de menu")
            opcion = int(input("Por favor ingrese una opcion\n"))
            
            if opcion == 1:
                nombre_perro = input("Por favor ingrese el nombre del perro: ")
                dueño = input("Por favor ingrese el nombre del dueño: ")
                domicilio = input("Por favor ingrese el domicilio: ")
                telefono = int(input("Por favor ingrese un telefono: "))
                motivo = int(input("por favor ingrese motivo de la visita:\n1_Baño\n2_Baño y Corte\n"))
                nuevo_perro = Perro(nombre_perro, dueño, domicilio, telefono, motivo)
                nuevo_perro.cargar_perro()     #el perro ingresado utiliza el metodo de carga de datos
                print("Perro cargado exitosamente")
                self.menu()
                
                
            if opcion == 2:
                buscado = input("ingrese nombre de perro a buscar:  ")
                opc = int(input("que desea modificar?:\n1_domicilio\n2_telefono\n3_ambos\n"))
                if opc == 1:
                    new_domicilio = input("ingrese nuevo domicilio:  ")
                    buscar = Conexiones()
                    buscar.abrirConexion()
                    buscar.miCursor.execute("UPDATE PERROS SET DOMICILIO= ? WHERE NOMBRE_PERRO = ?", (new_domicilio, buscado))
                    buscar.miConexion.commit()
                    buscar.cerrarConexion()
                elif opc == 2:
                    new_telefono = int(input("ingrese nuevo telefono:  "))
                    buscar = Conexiones()
                    buscar.abrirConexion()
                    buscar.miCursor.execute("UPDATE PERROS SET TELEFONO = ? WHERE NOMBRE_PERRO = ?", (new_telefono, buscado))
                    buscar.miConexion.commit()
                    buscar.cerrarConexion()
                else:
                    new_domicilio = input("ingrese nuevo domicilio:  ")
                    new_telefono = int(input("ingrese nuevo telefono:  "))
                    buscar = Conexiones()
                    buscar.abrirConexion()
                    #buscar.miCursor.execute("SELECT * FROM PERROS WHERE NOBRE_PERRO = ?", (buscado,))
                    buscar.miCursor.execute("UPDATE PERROS SET DOMICILIO= ?, TELEFONO = ? WHERE NOMBRE_PERRO = ?", (new_domicilio, new_telefono, buscado))
                    buscar.miConexion.commit()
                    buscar.cerrarConexion()
                print("Datos modificados correctamente")
                self.menu()
                
            if opcion == 3:
                eliminar = input("ingrese nombre de perro a eliminar:  ")
                eliminado = Conexiones()
                eliminado.abrirConexion()
                eliminado.miCursor.execute("DELETE FROM PERROS WHERE NOMBRE_PERRO = ?", (eliminar,))
                eliminado.miConexion.commit()
                eliminado.cerrarConexion()     
                print("Datos eliminados correctamente")
                self.menu()
                
            if opcion == 5:
                mostrar = Conexiones()
                mostrar.abrirConexion()
                mostrar.miCursor.execute("SELECT * FROM PERROS")
                lista = mostrar.miCursor.fetchall()
                print(lista)
                mostrar.miConexion.commit()
                mostrar.cerrarConexion()     
                self.menu()
           
            break
        
"""-------------------------------------------------------------------------------------------------------------------------"""
class Perro:
    def __init__(self, nombre_perro, dueño, domicilio, telefono, motivo):
        self.nombre_perro = nombre_perro
        self.dueño = dueño
        self.domicilio = domicilio
        self.telefono = telefono
        self.motivo = motivo
        
    def cargar_perro(self):
        conexion = Conexiones() # se crea objeto conexion de clse conexiones
        conexion.abrirConexion()    # objeto conexion utiliza los metodos de la clase conexiones
        conexion.miCursor.execute("INSERT INTO PERROS VALUES(NULL, '{}', '{}', '{}', '{}', '{}')".format(self.nombre_perro, self.dueño, self.domicilio, self.telefono, self.motivo))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
"""-------------------------------------------------------------------------------------------------------------------------"""

    
class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()


"""-------------------------------------------------------------------------------------------------------------------------"""
            
programa = ProgramaPrincipal()  #se crea objeto programa de clase prograam principal
programa.menu()    #el objeto menu utiliza el metodo menu para volver a llamar

