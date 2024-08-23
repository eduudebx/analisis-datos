# Eduardo Mendieta T.

productos = {''}

def registrar_datos_cli():
    datos = {}
    datos['cedula'] = input('Ingrese el número de cédula: ')
    datos['nombre'] = input('Ingrese el nombre: ')
    datos['apellido'] = input('Ingrese el napellido: ')
    datos['direccion'] = input('Ingrese la dirección: ')
    return datos


