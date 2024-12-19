'''
La encriptación asimétrica usa dos claves diferentes pero relacionadas: una clave pública para cifrar 
los datos y una clave privada para descifrarlos. La clave pública se puede compartir con cualquiera, 
mientras que la clave privada se mantiene en secreto. Si alguien  quiere enviar un mensaje seguro a otra,
persona, lo cifra con su clave pública. Solo la otra persona, con su clave privada, podrás descifrarlo. 
Este sistema es útil porque permite una comunicación segura sin necesidad de compartir previamente una clave secreta.
'''

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64


def generar_clave_rsa(tamano_clave):
    """
    Genera un par de claves RSA (clave pública y privada) de un tamaño específico. Utiliza el tamaño 
    de clave especificado en bits (128, 192 o 256 bits). La clave privada se genera primero y luego 
    se obtiene la clave pública asociada a ella. Si el tamaño de clave no es uno de los valores válidos, 
    se ajusta por defecto a 128 bits.

    Parámetros:
        tamano_clave (int): El tamaño de la clave en bits. Puede ser 1024, 2048, 4096 bits, esto debido a 
        que el tamaño minimo requerido para RSA es de 1024 

    Retorna:
        tuple: Una tupla que contiene:
            - clave_privada (RSAPrivateKey): La clave privada generada.
            - clave_publica (RSAPublicKey): La clave pública asociada a la clave privada.
    """
    tamano_clave = 1024 if tamano_clave not in (1024, 2048, 4096) else tamano_clave
    clave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=tamano_clave,  
        backend=default_backend()
    )
    clave_publica = clave_privada.public_key()
    return clave_privada, clave_publica


def encriptar_mensaje(clave_publica, mensaje):
    """
    Encripta un mensaje utilizando una clave pública RSA con padding OAEP. Toma un mensaje en texto plano y 
    lo cifra utilizando la clave pública RSA proporcionada. Utiliza el esquema de padding OAEP con el algoritmo 
    de hash SHA-256 para asegurar que el mensaje cifrado sea seguro y resistente a ataques.

    Parámetros:
        clave_publica (RSAPublicKey): La clave pública RSA utilizada para cifrar el mensaje.
        mensaje (str): El mensaje en texto plano que se desea encriptar.

    Retorna:
        bytes: El mensaje encriptado en formato binario.
    """
    mensaje_bytes = mensaje.encode('utf-8')
    
    mensaje_encriptado = clave_publica.encrypt(
        mensaje_bytes,
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )
    return mensaje_encriptado


def desencriptar_mensaje(clave_privada, mensaje_encriptado):
    """
    Desencripta un mensaje previamente encriptado utilizando la clave privada RSA y padding OAEP. 
    Toma un mensaje cifrado y lo descifra utilizando la clave privada RSA. El proceso de desencriptado 
    usa el mismo esquema de padding OAEP con SHA-256 que se utilizó en la encriptación, lo que garantiza 
    que el mensaje se recupere correctamente.

    Parámetros:
        clave_privada (RSAPrivateKey): La clave privada RSA utilizada para descifrar el mensaje.
        mensaje_encriptado (bytes): El mensaje encriptado que se desea desencriptar.

    Retorna:
        str: El mensaje desencriptado como una cadena de texto.
    """
    mensaje_desencriptado = clave_privada.decrypt(
        mensaje_encriptado,
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )
    return mensaje_desencriptado.decode('utf-8')


def main():
    """
    Función principal que genera un par de claves RSA, encripta un mensaje y luego lo desencripta.
    """
    tamano_clave = int(input('\nSelecciona el tamaño de la clave (1024, 2048 o 4096 bits): ')) 

    clave_privada, clave_publica = generar_clave_rsa(tamano_clave)

    print(f'Clave publica: {clave_publica}\n Clave privada: {clave_privada}\n')

    mensaje = input('\nIngresa un mensaje para cifrarlo: ')
    mensaje_encriptado = encriptar_mensaje(clave_publica, mensaje)

    print(f'\nMensaje encriptado: {base64.b64encode(mensaje_encriptado).decode("utf-8")}')
    print(f'\nMensaje desencriptado: {desencriptar_mensaje(clave_privada, mensaje_encriptado)}\n')


main()