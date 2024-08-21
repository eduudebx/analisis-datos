# Ejercicio 1: --------------------------------------------------
def relacion(a, b):
    if a > b: return 1
    elif a < b: return -1
    else: return 0


print(f'\nEjercicio 1: a = 10, b = 2, Respuesta: {relacion(10, 2)}.')
print(f'Ejercicio 1: a = 5, b = 10, Respuesta: {relacion(5, 10)}.')
print(f'Ejercicio 1: a = 3, b = 3, Respuesta: {relacion(3, 3)}.')


# Ejercicio 2: --------------------------------------------------
def factorial(num):
    respuesta = 1
    while num > 0:
        respuesta *= num
        num -= 1
    return respuesta


print(f'\nEjercicio 2: 4! = {factorial(4)}.')
print(f'Ejercicio 2: 5! = {factorial(5)}.')
print(f'Ejercicio 2: 6! = {factorial(6)}.')


# Ejercicio 3: --------------------------------------------------}
def calcular_imc(peso_kg, altura_m):
    if altura_m > 0: return round(peso_kg / altura_m ** 2, 1)
    return None


print(f'\nEjercicio 3: peso = 70kg, masa = 1.75m, IMC = {calcular_imc(70, 1.75)}')
print(f'Ejercicio 3: peso = 50kg, masa = 1.50m, IMC = {calcular_imc(50, 1.5)}')
print(f'Ejercicio 3: peso = 120kg, masa = 1.60m, IMC = {calcular_imc(120, 1.6)}')


# Ejercicio 4: --------------------------------------------------
def calcular_area_rectangulo(l1_cm, l2_cm):
    return l1_cm * l2_cm


print(f'\nEjercicio 4: lado 1 = 5cm, lado 2 = 3cm, Area = {calcular_area_rectangulo(5, 3)}cm2')
print(f'Ejercicio 4: lado 1 = 10cm, lado 2 = 7cm, Area = {calcular_area_rectangulo(10, 7)}cm2')
print(f'Ejercicio 4: lado 1 = 3.2cm, lado 2 = 7.5cm, Area = {calcular_area_rectangulo(3.2, 7.5)}cm2\n')


# Ejercicio 5: --------------------------------------------------
productos = {'Pan': 0.15, 'Leche': 0.9, 'Huevos': 0.1, 'Arroz': 0.75, 'Pollo': 1.2}


def imprimir_productos():
    print(f'\nProductos: precios = {productos}\n')


def ingresar_producto():
    imprimir_productos()
    producto = input('Ingresa el nombre del producto: ').capitalize()
    precio = float(input('Ingresa el precio en $: '))
    productos[producto] = precio
    imprimir_productos()


def facturar():
    cliente = input('Ingresa el nombre y apellido del cliente: ').capitalize()
    iva = float(input('Ingresa el valor del iva[0 - 1]: '))
    
    imprimir_productos()

    detalle = f'\n\nCliente: {cliente}\n\n------ DETALLE ------\n'
    cont_productos, total = 0, 0

    while True:
        producto = input('Ingrese el nombre del producto: ').capitalize()
        if producto in productos.keys():
            cantidad = int(input('Ingresa la cantidad: '))
            precio = productos[producto]
            total += round(precio * cantidad, 2)
            cont_productos += 1
            detalle += f'\n{cont_productos}. | {producto} | cantidad: {cantidad} | p/u: ${precio} | total: ${round(precio * cantidad, 2)}'
        else: print(f'\nEl producto [{producto}], no esta dentro de la lista de productos.')

        otro = input('\nIngrese la letra [a] para agregar otro producto al detalle u otra letra para salir: ').lower()
        if otro != 'a': break

    detalle += f'\n\nSubtotal: {total} | Iva {iva * 100}%: ${round(total * iva, 2)} '
    total = round(total + total * iva, 2)
    detalle += f'Total: ${total}\n'
    print(detalle)


facturar()