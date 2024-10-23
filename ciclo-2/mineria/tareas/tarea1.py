# Ejercicio 16 - Programa para imprimir el nombre del mes correspondiente a un número del 1 al 12:
numero = int(input('\nIngresa un número del 1 - 12: '))

meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio',
         7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}

if 1 <= numero <= 12:
    print(f'\n{numero} correspondes al mes de {meses.get(numero)}.\n')
else:
    print(f'\n{numero} no esta asociado con ningún mes del año.\n')


# Ejercicio 17 - Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla 
# la calificación según la siguiente tabla:
# 0-2: Muy deficiente, 3-4: Insuficiente, 5-6: Suficiente, 7: Bien, 8-9: Notable, 10: Sobresaliente.
nota = float(input('\nIngrese una nota del 0 - 10: '))

if 0 <= nota <= 2:
    print(f'\n{nota}: Muy deficiente.\n')
elif nota <= 4:
    print(f'\n{nota}: Insuficiente.\n')
elif nota <= 6:
    print(f'\n{nota}: Suficiente.\n')
elif nota == 7:
    print(f'\n{nota}: Bien.\n')
elif nota <= 9:
    print(f'\n{nota}: Notable.\n')
elif nota == 10:
    print(f'\n{nota}: Sobresaliente.\n')
else:
    print(f'\nLa nota {nota} no esta dentro del rango permitido [0-10].\n')


# Ejercicio 18 - Escribir un programa que pida al usuario una frase y determine si es un palíndromo. 
# Ignorar espacios en blanco y mayúsculas/minúsculas al determinar si la frase es un palíndromo o no. 
# Un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a 
# izquierda. Por ejemplo, "ana", "radar" y "aibohphobia" son palíndromos.
frase = input('\nIngrese una frase: ')

frase_aux = frase.lower().replace(' ', '')

if frase_aux == frase_aux[::-1]:
    print(f'\nLa frase "{frase}" SI es un Palíndromo.\n')
else:
    print(f'\nLa frase "{frase}" NO es un Palíndromo.\n')


# Ejercicio 19 - Escribir un programa que pida al usuario su nombre y edad, y muestre por pantalla un 
# mensaje con dichos datos en la siguiente forma: "Hola, {nombre}, tienes {edad} años".
nombre = input('\nIngresa tu nombre: ')
edad = int(input('\nIngresa tu edad: '))

print(f'\nHola, {nombre}, tienes {edad} años.\n')


# Ejercicio 20 - Escribir un programa que pregunte al usuario una cantidad de días y muestre por pantalla 
# cuantas horas, minutos y segundos hay en dicha cantidad de días.
dias = float(input('\nIngrese una cantidad de días: '))

if dias > 0:
    print(f'\n{dias} días es igual a {dias*24} en horas, {dias*24*60} en minutos y {dias*24*60*60} en segundos.\n')