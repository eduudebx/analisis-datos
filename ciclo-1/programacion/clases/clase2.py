# 1.Funciones y formateo de Strings:
cadena = '\tEcuador es un país maravilloso y \nCuenca es la ciudad más popular del país.' # Tabulación y salto de línea.
print('\nLongitud: ', len(cadena)) # Número de caracteres.
nombre, apellido, edad = 'Juanito', 'Alimaña', 22 
print('Mi nombre es {} {} y mi edad es {} años.'.format(nombre, apellido, edad))
print('Mi nombre es %s %s y mi edad es %d años.'%(nombre, apellido, edad))
print(f'Mi nombre es {nombre} {apellido} y mi edad es {edad} años.\n')


# 2.Funciones de corte:
cadena = 'Ecuador es un país maravilloso'
corte = cadena[0:7] # Desde la posición cero hasta la posición 6.
print(corte)
corte = cadena[14:] # Desde la posición 14 hasta el final de la cadena.
print(corte)
corte = cadena[-2:] # Desde el final contando 2 caracteres.
print(corte)
corte = cadena[1:6:2] # Desde la posición 1 hasta la posición 5, saltando 1 caracteres.
print(corte)
reverso = cadena[::-1] # Invierte la cadena.
print(reverso)