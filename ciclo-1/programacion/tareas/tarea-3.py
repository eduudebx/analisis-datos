lista_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lista_2 = lista_1[::-1]

print(f'\nLista 1: {lista_1} | Lista 2: {lista_2}')

pares, impares, multiplicaciones = [], [], []

for i in range(len(lista_1)):
    if lista_1[i] % 2 == 0:
        pares.append(lista_1[i])
    else:
        impares.append(lista_1[i])
    multiplicaciones.append(lista_1[i] * lista_2[i])

print(f'\nPares: {pares}\nImpares: {impares}\nMultiplicaciones: {multiplicaciones}\n')

