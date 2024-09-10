'''
1.	Crea una aplicación que nos genere una cantidad de números enteros aleatorios que nosotros le pasaremos por teclado. 
Crea un método donde pasamos como parámetros entre que números queremos que los genere, podemos pedirlas por teclado antes 
de generar los números. Este método devolverá un número entero aleatorio. Muestra estos números por pantalla.
'''
import random


def generar_numero_aleatoreo(limite_inferior, limite_superior):
    num_aleatoreo = random.randint(limite_inferior, limite_superior)
    return num_aleatoreo


def mostrar_numeros_aleatoreos(cantidad):
    limite_inferior = int(input('\nIngresa el límite inferior: '))
    limite_superior = int(input('Ingresa el límite superior: '))

    for i in range(cantidad):
        num_aleatoreo = generar_numero_aleatoreo(limite_inferior, limite_superior)
        print(f'Aleatoreo {i + 1}: {num_aleatoreo}.')


'''
2.	Crea una aplicación que nos pida un número por teclado y con un método se lo pasamos por parámetro para que nos indique
si es o no un número primo, debe devolver true si es primo sino false.Un número primo es aquel solo puede dividirse entre 1 
y si mismo. Por ejemplo: 25 no es primo, ya que 25 es divisible entre 5, sin embargo, 17 si es primo.
'''
def es_numero_primo(numero):
    es_primo = numero > 1
    divisor = numero - 1

    while divisor > 1:
        if numero % divisor == 0:
            es_primo = False
            break

        divisor = divisor - 1

    return es_primo


'''
3.	Crea una aplicación que nos convierta un número en base decimal a binario. Esto lo realizara un método al que le 
pasaremos el numero como parámetro, devolverá un String con el numero convertido a binario. Para convertir un numero 
decimal a binario, debemos dividir entre 2 el numero y el resultado de esa división se divide entre 2 de nuevo hasta 
que no se pueda dividir mas, el resto que obtengamos de cada división formara el numero binario, de abajo a arriba. 
Veamos un ejemplo: si introducimos un 8 nos deberá devolver 1000
'''
def decimal_a_binario(num_decimal):
    num_binario = '' if num_decimal > 0 else '0'

    while num_decimal > 0:
        num_binario += str(num_decimal % 2)
        num_decimal = num_decimal // 2

    return num_binario[::-1]


'''
4.	Crea un función que nos convierta una cantidad de euros introducida por teclado a otra moneda, estas pueden ser a dolares, 
yenes o libras. El método tendrá como parámetros, la cantidad de euros y la moneda a pasar que sera una cadena, este no 
devolverá ningún valor, mostrara un mensaje indicando el cambio.
'''
def mostrar_cambio_moneda(cantidad, tipo_moneda):
    equivalente = 0

    if tipo_moneda == 'dolares':
        equivalente = round(cantidad * 1.08, 2)
    elif tipo_moneda == 'yenes': 
        equivalente = round(cantidad * 153, 2)
    elif tipo_moneda == 'libras':
        equivalente = round(cantidad * 0.86, 2)

    print(f'\n{cantidad} euros = {equivalente} {tipo_moneda}\n')