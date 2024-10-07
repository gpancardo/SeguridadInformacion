import sqlite3
import generarNumero

def entradas():
    print("------------------------------------------------")
    print("")
    print("REGISTRO")
    print ("Crear un nuevo usuario")
    print("")
    print("------------------------------------------------")
    usuario=input("Ingrese un nombre de usuario: ")
    password=input("Ingrese una contraseña de 10 o más carácteres: ")
    if (len(password)<10):
        error=True
        while (error==True):
            print("Hay un problema con la longitud de su contraseña.")
            password=input("Ingrese una contraseña de 10 o más carácteres: ")
            if (len(password)>=10):
                error=False
    entradas=[usuario, password]
    return entradas

def escribirBase():
    entradasUso=entradas()
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute('''
INSERT INTO Usuario (nombre,  password) 
VALUES (?, ?)
''', (entradasUso[0], entradasUso[1]))
    conexion.commit()
    conexion.close()
    print("Se ha creado un nuevo usuario")
    print("Recuerda cuidar tu contraseña.")

def main():
    escribirBase()
    print("Se ha creado un archivo numero.secreto que es necesario para iniciar sesión.")
    generarNumero()