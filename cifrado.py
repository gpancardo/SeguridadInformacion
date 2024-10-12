def cesar(texto, cambio, cifrar=True):
    """
------------------------------------------------
CIFRADO CÉSAR
------------------------------------------------
    """
    resultado = []

    for letra in texto:
        if letra.isalpha():
            movimiento = ord('A') if letra.isupper() else ord('a')
            if cifrar:
                nuevo = chr((ord(letra) - movimiento + cambio) % 26 + movimiento)
            else:
                nuevo = chr((ord(letra) - movimiento - cambio) % 26 + movimiento)
            resultado.append(nuevo)
        else:
            resultado.append(letra)

    return ''.join(resultado)


def vigenere(texto, llave, cifrar=True):
    """
------------------------------------------------
CIFRADO VIGENERE
------------------------------------------------
    """
    texto = texto.replace(" ", "").upper()
    llave = llave.replace(" ", "").upper()

    resultado = []
    palabraRepetida = []

    # Crear la secuencia repetida de la llave
    i = 0
    for letra in texto:
        if letra.isalpha():
            palabraRepetida.append(llave[i % len(llave)])
            i += 1
        else:
            palabraRepetida.append(letra)

    # Cifrar o descifrar el texto
    for i, letra in enumerate(texto):
        if letra.isalpha():
            shift = ord(palabraRepetida[i]) - ord('A')
            if cifrar:
                nuevo = chr((ord(letra) - ord('A') + shift) % 26 + ord('A'))
            else:
                nuevo = chr((ord(letra) - ord('A') - shift) % 26 + ord('A'))
            resultado.append(nuevo)
        else:
            resultado.append(letra)

    return ''.join(resultado)