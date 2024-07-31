'''
Estudiante: EDuardo Mendieta T.
Ejercicio con listas.
'''

estudiantes = []
asignaturas = []

print('\n ---- Listado de Estudiantes ----\n')
for i in range(10):
    estudiantes.append(input(f'Ingrese el nombre del estudiante N°{i + 1}: '))

print('\n ---- Listado de asignaturas ----\n')
for i in range(5):
    asignaturas.append(input(f'Ingrese el nombre de la asignatura N°{i + 1}: '))

estudiantes.sort(reverse = True)
asignaturas.sort()

print(f'\nEstudiantes: {estudiantes}')
print(f'Asignaturas: {asignaturas}')

lista_completa = estudiantes + asignaturas

print(f'Lista completa: {lista_completa}\n')
