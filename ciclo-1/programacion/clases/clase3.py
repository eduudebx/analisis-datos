''' --------------------------- LISTAS EN PYTHON --------------------------- 
Son estructuras de datos que permiten almacenar una colección ordenada de elementos. 
Se caracterizan por ser mutables.
'''
lista = [1, 2, 3, 4, 5]

# 1.Método len():
print(f'\nLongitud de la lista{lista}: {len(lista)}.')


# 2.Acceso y busqueda:
print(f'\nAccediendo al primer elemento de la lista{lista}: {lista[0]}')
print(f'Accediendo al último elemento de la lista{lista}: {lista[-1]}')
print(f'Existe el elemnto 30 en la lista{lista}?: {30 in lista}')
print(f'La posición del elemnto 3 en la lista{lista} es {lista.index(3)}')
for elemento in lista: # Iterando sobre los elementos
    print(elemento)


# 3.Concatección:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(f'\nLista1: {lista1}, Lista2: {lista2}.')
print(f'Concatenar con +: {lista1 + lista2}')
lista1.extend(lista2)
print(f'Concatenar con extend(): {lista1}')
lista1 = [1, 2, 3]
lista1 += lista2
print(f'Concatenar con +=: {lista1}')


# 4.Operaciones crud:
lista = [10, 20, 30, 40, 50]
print(f'\nLista Creada: {lista}.')
print(f'Leer el elemento de la posición 0: {lista[0]}.')
lista[1] = -30
print(f'Actualizando la posición 1: {lista[1]}.')
del lista[1]
print(f'Eliminar con el operador del, eliminando -30: {lista}.')
lista.remove(40)
print(f'Eliminar con el método .remove(), eliminando 40: {lista}.')
lista.pop()
print(f'Eliminar con el método .pop(), eliminando el último elemento: {lista}.')


# 5.Operaciones con listas:
lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 2, 4, 10]
print(f'\nLista1: {lista1}, Lista2: {lista2}.')
copia1 = lista1[:] 
print(f'Copia de la lista1 con [:]: {copia1}.')
copia2 = list(lista2) 
print(f'Copia de la lista2 con la función list(): {copia2}.')
copia3 = lista1.copy()
print(f'Copia de la lista1 con el método .copy(): {copia3}.')

lista = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
print(f'\n{lista}')
lista = []
print(f'Limpiando igualando a una lista vacía: {lista}.')
lista = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
lista.clear()
print(f'Limpiando con el método .clear(): {lista}')

lista = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]
print(f'\nLista: {lista}')
lista.reverse()
print(f'Revertir con el método .reverse(): {lista}')
print(f'Revertir con el método slicing: {lista[::-1]}')

lista = [0, 15, 2, 33, 4, 50, 7, -8, -9, 10]
print(f'\nLista: {lista}.')
lista.sort()
print(f'Ordenamiento ascendente con el método .sort(): {lista}')
lista.sort(reverse = True)
print(f'Ordenamiento descendente con el método .sort(): {lista}')
lista = [0, 15, 2, 33, 4, 50, 7, -8, -9, 10]
print(f'Lista: {lista}.')
print(f'Ordenamiento ascendente con la función sorted(): {sorted(lista)}')
print(f'Ordenamiento descendente con la función sorted(): {sorted(lista, reverse = True)}')

# 6.Sub-listas -  Slicing:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'\nSub-lista con elementos de de las posiciones [2-4]: {lista[2:5]}')
print(f'Sub-lista con elementos de de las posiciones [0-3]: {lista[0:4]}')
print(f'Sub-lista con elementos de de las posiciones [5-8]: {lista[5:]}')
print(f'Copia de los elemntos con slicing: {lista[:]}\n')
