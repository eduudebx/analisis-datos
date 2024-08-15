# Ejercicio con Listas, Tuplas y Conjuntos: ------------------------------------------------

lista = []
tupla = ()
conjunto = set()


while True:
    print('\n----- BIENVENIDOS AL MENÚ -----')
    opcion = input('1.Listas\n2.Tuplas\n3.Conjuntos\n4.Salir\nElige una opción del menú: ')

    if opcion == '1':
        print('\n----- Operaciones con Listas -----\n')
        operacion = input('a.Crear lista\nb.Agregar elemento\nc.Eliminar elemento\nd.Imprimir lista\n¿Qué operación deseas realizar?: ')

        if operacion == 'a':
            num_elementos = int(input('\nCuantos elementos deseas en la lista: '))
            lista = []
            for i in range(num_elementos):
                lista.append(input(f'\nIngresa el elemento N°{i + 1}: '))
            print('\nOperación finalizada...')

        elif operacion == 'b':
            lista.append(input('\nIngresa un elemento: '))
            print('\nOperación finalizada...')

        elif operacion == 'c':
            elemento = input('\nIngrese el elemento que desea eliminar de la lista: ')
            while elemento in lista:
                lista.remove(elemento)
            print('\nOperación finalizada...')

        elif operacion == 'd':
            print(f'\nLista: {lista}\n\nOperación finalizada...')

        else:
            print('\nNo se realizo ninguna operación.')
        
    elif opcion == '2':
        print('\n----- Operaciones con Tuplas -----\n')
        operacion = input('a.Crear tupla\nb.Imprimir tupla\n¿Qué operación deseas realizar?: ')

        if operacion == 'a':
            num_elementos = int(input('\nCuantos elementos deseas en la tupla: '))
            lista, tupla = [], ()
            for i in range(num_elementos):
                lista.append(input(f'\nIngresa el elemento N°{i + 1}: '))

            tupla = tupla + tuple(lista)
            print('\nOperación finalizada...')

        elif operacion == 'b':
            print(f'\nTupla: {tupla}\n\nOperación finalizada...')

        else:
            print('\nNo se realizo ninguna operación.')

    elif opcion == '3':
        print('\n------ Operaciones con Conjuntos -----\n')
        operacion = input('a.Crear conjunto\nb.Agregar elemento\nc.Eliminar elemento\nd.Imprimir conjunto\n¿Qué operación deseas realizar?: ')

        if operacion == 'a':
            num_elementos = int(input('\nCuantos elementos deseas en el conjunto: '))
            conjunto = set()
            for i in range(num_elementos):
                conjunto.add(input(f'\nIngresa el elemento N°{i + 1}: '))
            print('\nOperación finalizada...')

        elif operacion == 'b':
            conjunto.add(input('\nIngresa un elemento: '))
            print('\nOperación finalizada...')

        elif operacion == 'c':
            elemento = input('\nIngrese el elemento que desea eliminar del conjunto: ')
            while elemento in conjunto:
                conjunto.remove(elemento)
            print('\nOperación finalizada...')

        elif operacion == 'd':
            print(f'\nConjunto: {conjunto}\n\nOperación finalizada...')

        else:
            print('\nNo se realizo ninguna operación.')

    elif opcion == '4':
        print('\nChao...\n')
        break
    
    else:
        print(f'\n[{opcion}] no esta entre la lista de opciones.\n')

    input('\nPresiona cualquier tecla para retornar al menú: ')
