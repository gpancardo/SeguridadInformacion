import os
import random

def numeroSecreto(password):
    if not os.path.exists(password):
        os.makedirs(password)

    numeroAzar = random.randint(1000, 9999)
    archivo = os.path.join(password, "numero.secreto")

    with open(archivo, 'w') as file:
        file.write(str(numeroAzar))

    if os.path.exists(archivo):
        print(f"La llave se ha creado con éxito.")
    else:
        print("Ha habido un error, intenta de nuevo.")