abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q',
              'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lista_reducida = []

for i in range(1, len(abecedario) + 1):
    if i % 3 != 0:
        lista_reducida.append(abecedario[i - 1])


print(f'\nLista reducida: {lista_reducida}\n')
