'''
La encriptación híbrida combina dos enfoques de cifrado: cifrado simétrico y cifrado asimétrico. 
Aprovechar las ventajas de ambos métodos para lograr un sistema de cifrado eficiente y seguro.
'''

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as padding_utils
import os
import base64



def generar_claves_rsa():
    """
    Genera un par de claves RSA (clave pública y clave privada) de 2048 bits.
    Utiliza el módulo rsa de la biblioteca cryptography para generar una clave privada RSA con un 
    exponente público de 65537 y un tamaño de clave de 2048 bits. A partir de la clave privada generada, 
    se obtiene la clave pública correspondiente.

    Retorna:
        tuple: Una tupla que contiene dos elementos:
            - private_key (RSAPrivateKey): La clave privada generada.
            - public_key (RSAPublicKey): La clave pública generada.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def cifrar_aes(mensaje, clave_aes):
    """
    Cifra un mensaje utilizando el algoritmo AES en modo CBC con una clave AES proporcionada.
    Utiliza el algoritmo AES en modo CBC con un vector de inicialización (IV) aleatorio y realiza el 
    relleno del mensaje usando el esquema PKCS7 para que el mensaje tenga una longitud múltiplo de 16 bytes 
    antes de ser cifrado. El mensaje cifrado es devuelto junto con el IV utilizado.

    Parámetros:
        mensaje (str): El mensaje de texto plano que se desea cifrar.
        clave_aes (bytes): La clave AES de 16, 24 o 32 bytes utilizada para el cifrado.

    Retorna:
        tuple: Una tupla que contiene dos elementos:
            - iv (bytes): El vector de inicialización (IV) utilizado en el cifrado.
            - mensaje_cifrado (bytes): El mensaje cifrado en formato binario.
    """
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(clave_aes), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding_utils.PKCS7(algorithms.AES.block_size).padder()
    mensaje_padded = padder.update(mensaje.encode()) + padder.finalize()
    mensaje_cifrado = encryptor.update(mensaje_padded) + encryptor.finalize()
    return iv, mensaje_cifrado


def cifrar_clave_aes(clave_aes, clave_publica_rsa):
    """
    Cifra una clave AES utilizando una clave pública RSA.
    Utiliza la clave pública RSA y el algoritmo de relleno OAEP con SHA-256 para cifrar la clave AES 
    de manera segura. Esto permite que la clave AES pueda ser transmitida de forma segura junto con 
    el mensaje cifrado, utilizando el cifrado asimétrico.

    Parámetros:
        clave_aes (bytes): La clave AES de 16, 24 o 32 bytes que se desea cifrar.
        clave_publica_rsa (RSAPublicKey): La clave pública RSA que se utilizará para cifrar la clave AES.

    Retorna:
        bytes: La clave AES cifrada utilizando RSA.
    """
    clave_cifrada = clave_publica_rsa.encrypt(
        clave_aes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return clave_cifrada


def descifrar_clave_aes(clave_cifrada_rsa, clave_privada_rsa):
    """
    Desencripta una clave AES cifrada utilizando una clave privada RSA.
    Utiliza la clave privada RSA junto con el algoritmo de relleno OAEP con SHA-256 para descifrar 
    una clave AES cifrada previamente con la clave pública RSA. La clave AES descifrada es utilizada 
    para descifrar el mensaje.

    Parámetros:
        clave_cifrada_rsa (bytes): La clave AES cifrada utilizando RSA.
        clave_privada_rsa (RSAPrivateKey): La clave privada RSA utilizada para descifrar la clave AES.

    Retorna:
        bytes: La clave AES descifrada.
    """
    clave_aes = clave_privada_rsa.decrypt(
        clave_cifrada_rsa,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return clave_aes


def descifrar_aes(iv, mensaje_cifrado, clave_aes):
    """
    Desencripta una clave AES cifrada utilizando una clave privada RSA.
    Utiliza la clave privada RSA junto con el algoritmo de relleno OAEP con SHA-256 para descifrar 
    una clave AES cifrada previamente con la clave pública RSA. La clave AES descifrada es utilizada 
    para descifrar el mensaje.

    Parámetros:
        clave_cifrada_rsa (bytes): La clave AES cifrada utilizando RSA.
        clave_privada_rsa (RSAPrivateKey): La clave privada RSA utilizada para descifrar la clave AES.

    Retorna:
        bytes: La clave AES descifrada.
    """
    cipher = Cipher(algorithms.AES(clave_aes), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    mensaje_descifrado = decryptor.update(mensaje_cifrado) + decryptor.finalize()
    unpadder = padding_utils.PKCS7(algorithms.AES.block_size).unpadder()
    mensaje = unpadder.update(mensaje_descifrado) + unpadder.finalize()
    return mensaje.decode()


def main():
    """
    Función principal que permite al usuario cifrar y descifrar un mensaje utilizando un esquema híbrido de 
    cifrado con RSA y AES.
    """
    clave_privada_rsa, clave_publica_rsa = generar_claves_rsa()
    clave_aes = os.urandom(32)
    
    mensaje = input('\nIngresa un mensaje para cifrarlo: ')
    iv, mensaje_cifrado = cifrar_aes(mensaje, clave_aes)

    clave_cifrada_rsa = cifrar_clave_aes(clave_aes, clave_publica_rsa)
    
    print(f'\nMensaje cifrado (base64): {base64.b64encode(mensaje_cifrado).decode()}\n')
    print(f'\nClave AES cifrada con RSA (base64): {base64.b64encode(clave_cifrada_rsa).decode()}\n')
    
    clave_descifrada_aes = descifrar_clave_aes(clave_cifrada_rsa, clave_privada_rsa)
    print(f'\nMensaje descifrado: {descifrar_aes(iv, mensaje_cifrado, clave_descifrada_aes)}\n')


main()