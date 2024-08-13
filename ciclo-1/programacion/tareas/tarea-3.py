numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
numeros_2 = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

pares = [i for i in numeros if i % 2 == 0]

impares = [i for i in numeros if i % 2 != 0]

multiplicaciones = [numeros[i] * numeros_2[i] for i in range(len(numeros))]

print(f'\nLista1: {numeros}\nLista2: {numeros_2}\n\nPares: {pares}\nImpares: {impares}\nMultiplicaciones: {multiplicaciones}\n')

