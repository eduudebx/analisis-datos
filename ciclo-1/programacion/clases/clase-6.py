# Tuplas : ----------------------------------------------------------------
# Creación de menus: -------------------------------------
# Ejercicio con Listas, Tuplas y Conjuntos: ------------------------------------------------
import time


while True:
    print('\n----- BIENVENIDOS AL MENÚ -----')
    opcion = input('1.Listas\n2.Tuplas\n3.Conjuntos\n4.Salir\n¿Qué operación deseas realizar?: ')

    if opcion == '1':
        print('\n----- Operaciones con Listas -----\n')
        
    elif opcion == '2':
        print('\n----- Operaciones con Tuplas -----\n')

    elif opcion == '3':
        print('\n------ Operaciones con Conjuntos -----\n')

    elif opcion == '4':
        print('\nChao...\n')
        time.sleep(1)
        break
    else:
        print(f'\n[{opcion}] no esta entre la lista de opciones.\n')

    time.sleep(1.5)
    input('\nPresiona cualquier tecla para retornar al menú: ')
