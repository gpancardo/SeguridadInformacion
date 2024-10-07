import os
def redireccion(estado):
    if (estado=="escogerCifrado"):
        os.system("python escogerCifrado.py")
    elif (estado=="inicioSesion"):
        os.system("python inicioSesion.py")
    elif (estado=="registro"):
        os.system("python registro.py")
    elif (estado=="salir"):
        exit()
    else:
        os.system("python menu.py")