'''
El hashing es un proceso de encriptación unidireccional que toma una entrada como un mensaje o archivo
y la convierte en un valor de longitud fija. A diferencia de la encriptación asimétrica o simétrica, 
no se puede "desencriptar" un hash, pero se puede utilizar para verificar la integridad de los datos o 
almacenar contraseñas de manera segura.
'''

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64



def generar_hash(mensaje, tamano_hash):
    """
    Genera un hash de un mensaje utilizando el algoritmo SHA-256 y ajustado al tamaño de hash solicitado. 
    Calcula un hash criptográfico de un mensaje utilizando el algoritmo SHA-256. El tamaño del hash 
    resultante se ajusta a uno de los siguientes tamaños en bits: 128, 192 o 256. Si el tamaño solicitado 
    no es uno de estos, se utiliza el tamaño de hash completo (256 bits). El mensaje es primero codificado 
    en UTF-8 antes de ser procesado por el algoritmo de hash.

    Parámetros:
        mensaje (str): El mensaje de texto para el cual se desea generar el hash.
        tamano_hash (int): El tamaño del hash en bits. Debe ser 128, 192 o 256. 
                        El tamaño especificado define cuántos primeros bits del hash completo se retornarán.

    Retorna:
        bytes: Un hash truncado (o completo) de tamaño `tamano_hash` bits. Si el tamaño solicitado es 128, 192 
        o 256 bits, se devuelve el hash correspondiente de longitud adecuada.
    """
    128 if tamano_hash not in ( 128, 192, 256) else tamano_hash
    hash_obj = hashes.Hash(hashes.SHA256(), backend=default_backend())
    hash_obj.update(mensaje.encode('utf-8'))
    hash_completo = hash_obj.finalize()

    if tamano_hash == 128:
        hash = hash_completo[:16]
    elif tamano_hash == 192:
        hash = hash_completo[:24]
    else:
        hash = hash_completo
    
    return hash


 # Convertimos el hash a base64 para que sea legible
mostrar_hash_base64 = lambda hash: base64.b64encode(hash).decode('utf-8')


def main():
    """
    Función principal que solicita un mensaje al usuario, genera un hash y lo convierte a base64.
    """
    mensaje = input('\nIngresa un mensaje para cifrarlo: ')
    
    tamano_hash = int(input('\nSelecciona el tamaño del hash (128, 192 o 256 bits): '))

    hash = generar_hash(mensaje, tamano_hash)

    print(f'\nHash en base64: {mostrar_hash_base64(hash)}\n')


main()