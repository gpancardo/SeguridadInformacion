import sqlite3
import os
import redireccion

def recibirInformacion():
    print("------------------------------------------------")
    print("")
    print("INICIO DE SESIÓN")
    print ("Acceder a los servicios de encriptación")
    print("")
    print("------------------------------------------------")
    usuario=input("Ingresa tu usuario: ")
    password=input("Ingrese contraseña: ")
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    cursor.execute('SELECT nombre, password FROM Usuario WHERE  nombre = ? AND password = ?', (usuario, password))
    usuarioRecibido = cursor.fetchone()
    if (usuarioRecibido):
        print("Bienvenido/a, "+str(usuarioRecibido[0]))
        numeroSecreto=int(input("Podrías proporcionar tu número secreto? "))
        carpeta = os.path.join(usuario, "numero.secreto")
        with open(carpeta, 'r') as archivo:
            numeroSecretoReal = archivo.read()
            numeroSecretoReal=int(numeroSecretoReal)
        if (numeroSecreto==numeroSecretoReal):
            redireccion.redireccion("escogerCifrado")
        else:
            print("No puedes iniciar sesión sin el número secreto correcto.")
    else:
        print("La información es incorrecta.")
        salir=input("Quiere regresar al menu principal? S/N ")
        if (salir.upper()=="S"):
            redireccion.redireccion("")
        recibirInformacion()
    conexion.close()


recibirInformacion()