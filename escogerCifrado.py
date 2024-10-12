import cifrado

def opcionEncontrar():
    opcion=input("""Qué sistema de encriptación quieres usar? 
                
    --CÉSAR (C)
    --VIGENERE (V)
                
O--+ """)

    opcion=opcion.upper()
    quiereCifrar=input("Quieres cifrar o decifrar? C/D ")
    quiereCifrar=quiereCifrar.upper()
    texto=input("Ingrese el mensaje: ")
    if (quiereCifrar=="C"):
        cifrar=True
    else:
        cifrar=False

    if (opcion=="C"):
        cambio=int(input("Ingrese el cambio: "))
        recibe=cifrado.cesar(texto, cambio, cifrar)
    elif (opcion=="V"):
        llave=input("Ingrese llave: ")
        recibe=cifrado.vigenere(texto, llave, cifrar)
    else:
        opcionEncontrar()
    return recibe

final=opcionEncontrar()

print("El mensaje cifrado es "+final)