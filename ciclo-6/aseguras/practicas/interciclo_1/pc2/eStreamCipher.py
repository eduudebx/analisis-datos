'''
Son algoritmos de cifrado simétrico que encriptan datos de manera bit a bit o byte a byte, 
generalmente utilizando una clave de longitud fija y un generador de claves que produce una 
secuencia pseudoaleatoria de bits, llamada keystream, que se combina con el 
texto plano mediante una operación XOR.
'''


from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64


def cifrar_mensaje(mensaje, clave, nonce):
    """
    Cifra un mensaje utilizando el algoritmo ChaCha20 con una clave y un nonce específicos. 
    Toma un mensaje de texto y lo cifra utilizando el algoritmo ChaCha20, que es un algoritmo 
    de cifra de flujo. Se requiere una clave secreta y un nonce (número único utilizado una sola vez)
    para generar el flujo de claves que cifrará el mensaje. El mensaje es codificado en UTF-8 
    antes de ser cifrado.

    Parámetros:
        mensaje (str): El mensaje de texto que se desea cifrar.
        clave (bytes): La clave secreta de longitud adecuada.
        nonce (bytes): El valor nonce de 8 bytes que se utiliza para asegurar la unicidad del cifrado.

    Retorna:
        bytes: El mensaje cifrado en formato binario (bytes).
    """
    cipher = ChaCha20.new(key=clave, nonce=nonce)
    mensaje_cifrado = cipher.encrypt(mensaje.encode('utf-8'))
    return mensaje_cifrado


def descifrar_mensaje(mensaje_cifrado, clave, nonce):
    """
    Descifra un mensaje previamente cifrado utilizando el algoritmo ChaCha20 con la misma clave y nonce. 
    Toma un mensaje cifrado y lo descifra utilizando el algoritmo ChaCha20, utilizando la misma clave 
    y el mismo nonce que se usaron para cifrar el mensaje. El mensaje cifrado es desencriptado 
    y se devuelve como texto.

    Parámetros:
        mensaje_cifrado (bytes): El mensaje cifrado que se desea descifrar.
        clave (bytes): La clave secreta utilizada para cifrar y descifrar el mensaje.
        nonce (bytes): El nonce de 8 bytes que debe coincidir con el usado en el cifrado.

    Retorna:
        str: El mensaje original desencriptado como una cadena de texto.
    """
    cipher = ChaCha20.new(key=clave, nonce=nonce)
    mensaje_desencriptado = cipher.decrypt(mensaje_cifrado).decode('utf-8')
    return mensaje_desencriptado


# mensaje cifrado en base64.
mostrar_mensaje_base64 = lambda mensaje: base64.b64encode(mensaje).decode('utf-8')


def main():
    """
    Función principal que permite al usuario cifrar y descifrar un mensaje utilizando el algoritmo ChaCha20.
    El algoritmo ChaCha20 requiere que la clave tenga una longitud específica de 32 bytes (256 bits).
    """
    mensaje = input('\nIngresa un mensaje para cifrarlo: ')
    
   
    tamano_clave = 256 
    
    clave = get_random_bytes(32)
    print(f'\nClave generada ({tamano_clave} bits): {base64.b64encode(clave).decode("utf-8")}\n')
    
    nonce = get_random_bytes(8)
    print(f'\nNonce generado: {base64.b64encode(nonce).decode("utf-8")}\n')

    mensaje_cifrado = cifrar_mensaje(mensaje, clave, nonce)


    print(f'\nMensaje cifrado: {mostrar_mensaje_base64(mensaje_cifrado)}\n')
    print(f'\nMensaje desencriptado: {descifrar_mensaje(mensaje_cifrado, clave, nonce)}\n')



main()