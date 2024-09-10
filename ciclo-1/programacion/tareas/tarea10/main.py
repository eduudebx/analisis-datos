import funciones as fn
import os

while True:
    print('\n*******************  MENÚ  *******************\n',
          '1. Generar números aleatoreos.\n',
          '2. ¿Es un número primo?.\n',
          '3. Transformar de decimal a binario.\n',
          '4. Equivalente de euros con otras monedas.\n',
          'Presiona otra tecla para salir.')

    opcion = input('\nIngrese una de la opciones: ')
    os.system('clear')

    if opcion == '1':
        print('\n--------------- ALEATOREOS ---------------\n')
        fn.mostrar_numeros_aleatoreos(int(input('¿Cuantos números aleatoreos deseas generar?: ')))
    
    elif opcion == '2':
        print('\n----------------- PRIMOS -----------------\n')
        numero = int(input('Ingresa un número entero positivo: '))
        print(f'\n¿{numero} es un número primo?: {fn.es_numero_primo(numero)}.')

    elif opcion == '3':
        print('\n---------------- BINARIO -----------------\n')
        numero = int(input('Ingresa un número entero positivo: ')) 
        print(f'\n{numero} = {fn.decimal_a_binario(numero)}.')
    
    elif opcion == '4':
        print('\n----------------- MONEDA -----------------\n')
        cantidad = int(input('Ingrese la cantidad de euros: '))
        tipo_moneda = input('1. Dolares\n2. Yenes\n3. Libras\nIngresa el nombre de la moneda[ejm, Dolares]: ')
        fn.mostrar_cambio_moneda(cantidad, tipo_moneda.lower())
    
    else:
        print('\n\nAdioooos!\n\n')
        break

    input('\nPresiona cualquier tecla para retornar al menú.')
    os.system('clear')