def get_datos_cliente():
    datos = {}
    datos['cedula'] = input('Ingrese la cédula: ')
    datos['nombre'] = input('Ingrese el nombre: ').capitalize()
    datos['apellido'] = input('Ingrese el apellido: ').capitalize()
    datos['direccion'] = input('Ingrese la dirección: ').capitalize()
    return datos


def get_datos_producto():
    datos = {}
    datos['descripcion'] = input('\nIngrese el nombre del producto: ').capitalize()
    datos['precio'] = float(input('Ingrese el precio: '))
    datos['cantidad'] = int(input('Ingrese la cantidad: '))
    return datos


def get_linea_detalle(producto):
    total = producto['precio'] * producto['cantidad']
    linea = f'{producto["descripcion"]} | p/u: ${producto["precio"]} | total: ${total}'
    return linea, total


def facturar():
    iva = float(input('\nIngrese el valor del iva [0-1]: '))
    cliente = get_datos_cliente()
    detalle = '\n'
    total = 0

    print('\n\n ------ AGREGAR PRODUCTOS AL DETALLE ------\n')
    
    cont_ln_detalle = 1
    while True:
        linea, valor = get_linea_detalle(get_datos_producto())
        detalle += f'\n {cont_ln_detalle} | {linea}'
        total += valor
        cont_ln_detalle += 1

        ag_nuevo_producto = input('Desea agregar un nuevo producto? [si - otro = no]: ').lower()

        if ag_nuevo_producto != 'si':
            break
        
    detalle += f'\n\nSubTotal: {total}\nIva {iva * 100}: ${round(total * iva, 2)}\nDescuento: $2'
    total += round(total * iva, 2) - 2
    detalle += f'\nTotal: ${total}\n'

    print('\n\n ------------ FACTURA ------------ \n\n')
    print(f'Cedula: {cliente["cedula"]}\nCliente: {cliente["nombre"]} {cliente["apellido"]}\nDirección: {cliente["direccion"]}\n')
    print(f'\n ------------ DETALLE ------------ \n{detalle}\n')
