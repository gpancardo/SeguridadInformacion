import sqlite3
import generarNumero
import redireccion

entradas = []

def recibirEntradas():
    global entradas
    
    print("------------------------------------------------")
    print("")
    print("REGISTRO")
    print("Crear un nuevo usuario")
    print("")
    print("------------------------------------------------")
    
    usuario = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña de 10 o más caracteres: ")
    
    while len(password) < 10:
        print("Hay un problema con la longitud de su contraseña.")
        password = input("Ingrese una contraseña de 10 o más caracteres: ")
    
    entradas = [usuario, password]

def escribirBase():
    recibirEntradas()
    
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    INSERT INTO Usuario (nombre, password) 
    VALUES (?, ?)
    ''', (entradas[0], entradas[1]))
    
    conexion.commit()
    
    conexion.close()
    
    print("Se ha creado un nuevo usuario")
    print("Recuerda cuidar tu contraseña.")

def main():
    escribirBase()
    generarNumero.numeroSecreto(entradas[0])
    redireccion.redireccion("")

main()