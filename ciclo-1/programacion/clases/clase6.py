# Funciones: -----------------------------------------------------------

def hola():
    print('\nHola mundo!\n')


def saludar(nombre, edad):
    print(f'Hola {nombre} tienes {edad} años.')


def pedir_datos():
    nombre = input('\nIngresa tu nombre: ')
    edad = int(input('\nIngresa tu edad: '))
    return nombre, edad


def solicitar_enteros(n):
    numeros = []
    for i in range(n):
        numeros.append(int(input(f'{i + 1}) Ingresa un número: ')))
    return numeros


def realizar_operacion(opc, num1, num2):
    resultado = ''
    if opc == 1: resultado = f'{num1} + {num2} = {num1 + num2}'
    elif opc == 2: resultado = f'{num1} - {num2} = {num1 - num2}'
    elif opc == 3: resultado = f'{num1} x {num2} = {num1 * num2}'
    else:
        if num2 != 0: resultado = f'{num1} / {num2} = {num1 / num2}'
        else: resultado = 'No se puede dividir por cero!'
    return resultado 
      

def dividir(dividendo, divisor):
    if dividendo > divisor:
        print(f'{dividendo} / {divisor} = {dividendo/ divisor}')
    else:
        print('Operación Fallida !!!')
