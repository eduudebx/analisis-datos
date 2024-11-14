'''
La encriptación simétrica es un proceso en el que se utiliza la misma clave tanto para cifrar como para 
descifrar la información. Como un candado y una llave: la clave es la llave, y el mensaje cifrado es como 
un candado cerrado. Solo la persona que tenga la misma clave podrá descifrar el mensaje. Es rápida y eficiente, 
pero el mayor desafío es asegurarse de que ambas partes (quien cifra y quien descifra) mantengan la clave en secreto.
'''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os



def generar_clave(tamano_clave):
    """
    Genera una clave aleatoria de longitud variable para el algoritmo AES.

    Parámetros:
        tamano_clave (int): El tamaño de la clave deseada en bits. Debe ser uno de los siguientes valores:
                            128, 192 o 256.

    Retorna:
        bytes: Una clave aleatoria generada con el tamaño especificado en bytes (16, 24 o 32 bytes).
    """
    if tamano_clave == 192:
        return os.urandom(24) 
    elif tamano_clave == 256:
        return os.urandom(32) 
    else:
         return os.urandom(16)
        


def encriptar(mensaje, clave):
    """
    Encripta un mensaje utilizando el algoritmo AES en modo CBC con una clave proporcionada. 
    Se utiliza la encriptación simétrica con AES (Advanced Encryption Standard) en modo CBC 
    (Cipher Block Chaining). El mensaje se rellena con espacios para que su longitud sea un múltiplo 
    de 16 bytes, ya que el algoritmo AES requiere bloques de tamaño fijo. La función genera un vector 
    de inicialización (IV) aleatorio de 16 bytes y lo utiliza junto con la clave para cifrar el mensaje.

    Parámetros:
        mensaje (str): El mensaje de texto plano que se desea encriptar.
        clave (bytes): La clave secreta utilizada para el cifrado. Debe tener una longitud adecuada para 
        AES (16, 24 o 32 bytes).

    Retorna:
        tuple: Una tupla que contiene dos elementos:
            - iv (bytes): El vector de inicialización (IV) utilizado en el cifrado.
            - mensaje_encriptado (bytes): El mensaje encriptado en formato binario.
    """
    iv = os.urandom(16)  # Vector de inicialización aleatorio de 16 bytes
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv))
    encriptador = cifrador.encryptor()
    mensaje_relleno = mensaje + (16 - len(mensaje) % 16) * " "
    mensaje_encriptado = encriptador.update(mensaje_relleno.encode()) + encriptador.finalize()
    return iv, mensaje_encriptado


def desencriptar(iv, mensaje_encriptado, clave):
    """
    Desencripta un mensaje previamente encriptado utilizando el algoritmo AES en modo CBC con la misma clave 
    y vector de inicialización. Se utiliza el algoritmo AES en modo CBC para revertir el proceso de encriptación. 
    Recibe el vector de inicialización (IV) y el mensaje encriptado, y los usa junto con la clave para restaurar 
    el mensaje original. El mensaje desencriptado se limpia de cualquier relleno (espacios) al final del mensaje 
    antes de ser retornado.

    Parámetros:
        iv (bytes): El vector de inicialización utilizado durante la encriptación.
        mensaje_encriptado (bytes): El mensaje encriptado en formato binario que se desea desencriptar.
        clave (bytes): La clave secreta utilizada para el cifrado y descifrado. Debe ser la misma que la 
        utilizada para encriptar el mensaje.

    Retorna:
        str: El mensaje desencriptado como una cadena de texto, sin los rellenos agregados durante la encriptación.
    """
    cifrador = Cipher(algorithms.AES(clave), modes.CBC(iv))
    desencriptador = cifrador.decryptor()
    mensaje_desencriptado = desencriptador.update(mensaje_encriptado) + desencriptador.finalize()
    return mensaje_desencriptado.decode().rstrip()


def main():
    """
    Función principal que genera una clave secreta, encripta un mensaje y luego lo desencripta para mostrar 
    el resultado.
    """
    tamano_clave = int(input('\nSelecciona el tamaño de la clave (128, 192 o 256 bits): '))
    clave = generar_clave(tamano_clave)

    print(f'\nClave secreta ({tamano_clave} bits): {clave.hex()}\n')

    mensaje = input('\nIngresa un mensaje para cifrarlo: ')

    iv, mensaje_encriptado = encriptar(mensaje, clave)

    print(f'\nMensaje encriptado: {mensaje_encriptado.hex()}')
    print(f'Mensaje desencriptado: {desencriptar(iv, mensaje_encriptado, clave)}\n')


main()
