library(plotrix)
library(readxl)


datos <- read_excel('datos/datos-tarea-3.xlsx', sheet = 'Sheet1')

carreras <- datos[[1]]
num_estudiantes <- datos[[2]]

pie3D(num_estudiantes, labels = carreras, explode = 0.1, main = 'Estudiantes por carrera')
