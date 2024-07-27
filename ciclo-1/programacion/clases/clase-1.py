# 1.Hola mundo desde python:
print('Hola Python!')


# 2.Comentarios:
""" Comentario multilinea! """
''' Puedo seguir documentando mi código! '''


# 3.Tipos de datos:
print(type('\nEduardo')) # Tipo str.
print(type(5)) # Tipo int.
print(type(1.5)) # Tipo float.
print(type(3 + 1j)) # Tipo complex.
print(type(True)) # Tipo bool.
print(type(print('Cadena de texto'))) # Tipo NoneType.


# 4.Declaracion de variables:
nombre = 'Juanito'
print('\n', nombre)
edad = 22
print(edad)
sueldo = 950.99
print(sueldo)
escasado = False
print(escasado, '\n')


# 5.Funciones básicas:
print(len(nombre)) # longitud de caracteres.
cedula, apellido, estado_civil = '0105894756', 'Alimaña', 1 # Declaración de variables en una sola línea.
print('Los datos ingresados son, cedula: ', cedula, ', apellido: ', apellido, ', estado civil: ', estado_civil, '.') # Parámetros de la función print.


# 6.Ingreso de datos:
nombre = input('\nIngresa tu nombre: ')
edad = input('Ingresa tu edad: ')
print(f'Nombre: {nombre}, edad: {edad}.\n')


# 7.Operaciones Aritmeticas:
print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 % 4)
print(3 // 4)
print(3 ** 4)
print(2 ** 3 + 3 - 7 / 1 // 4)


# 8.Operacciones con cadenas de texto:
print('\nHola ' + 'Pytho ' + 'que tal!')
print('Número: ' + str(5))
print('Hola ' * 5, '\n')


# 9.Operaciones de comparación:
print(1 > 2)
print(1 >= 2)
print(1 < 2)
print(1 <= 2)
print(1 == 2)
print(1 != 2)


