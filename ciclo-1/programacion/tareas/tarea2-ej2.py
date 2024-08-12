num_asignaturas = int(input('\nIngresa el número de asignaturas evaluadas: '))

asignaturas = []
notas_medias = []
suspensos = []
alumnos_asignatura = []


print('\n')
for i in range(num_asignaturas):
    asignaturas.append(input(f'Ingresa el nombre de la asignatura N°{i + 1}: '))


print('\n')
for asignatura in asignaturas:
    media = 0
    num_suspensos = 0
    num_alumnos = int(input(f'\nIngresa el número de alumnos para la asignatura {asignatura}: '))
    for i in range(num_alumnos):
        nota = float(input(f'{asignatura} | Ingrese la nota sobre 10 para el alumno N°{i + 1}: '))
        if nota < 7: num_suspensos += 1
        media += nota
    notas_medias.append(media/num_alumnos)
    suspensos.append(num_suspensos)
    alumnos_asignatura.append(num_alumnos)


print('\nResultado de las evaluaciones de este año: ')
for i in range(num_asignaturas):
    print(f'Asignatura: {asignaturas[i]} | No. Alumnos: {alumnos_asignatura[i]} | Nota media: {round(notas_medias[i], 2)} | Suspensos: {suspensos[i]}')