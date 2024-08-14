# Creación de menus: -------------------------------------
import time


while True:
    print('\n----- BIENVENIDOS AL MENÚ -----')
    opcion = input('\n1.Pares e impares\n2.Sumas\n3.Serie de Fibonacci\n4.Salir\n\n¿Qué operación deseas realizar?: ')
    if opcion == '1':
        print('\n----- Pares e impares -----\n')
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        pares, impares = [], []
        for i in numeros:
            if i % 2 == 0: pares.append(i)
            if i % 2 == 1: impares.append(i)
        print(f'\nPares: {pares}\nImpares: {impares}\n')
    elif opcion == '2':
        print('\n----- Suma de 2 números -----\n')

    elif opcion == '3':
        print('\n------ Serie Fibonacci -----\n')

    elif opcion == '4':
        print('\nChao...\n')
        time.sleep(1)
        break
    else:
        print(f'\n[{opcion}] no esta entre la lista de opciones.\n')

    time.sleep(1.5)
    input('\nPresiona cualquier tecla para retornar al menú: ')
    
