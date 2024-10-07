import os
import random

def numeroSecreto(usuario):
    if not os.path.exists(usuario):
        os.makedirs(usuario)

    numeroAzar = random.randint(1000, 9999)
    archivo = os.path.join(usuario, "numero.secreto")

    with open(archivo, 'w') as file:
        file.write(str(numeroAzar))

    if os.path.exists(archivo):
        print(f"La llave se ha creado con éxito.")
        print("Tu número secreto es "+str(numeroAzar)+". Recuerda guardar ese número.")
    else:
        print("Ha habido un error, intenta de nuevo.")