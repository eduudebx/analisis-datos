library(readxl)
library(dplyr)


main <- function(){

    datos <- read_excel('ds-ventallantas-original.xlsx')
    #View(datos)

    #num_filas <- nrow(datos)
    #print(paste('El dataset a limpiar tiene:',  num_filas, 'filas.'))
    # El dataset a limpiar tiene:  127266  filas.

    #filas_blancas <- sum(apply(datos, 1, function(x) all(is.na(x) | x == '')))
    #print(paste('El dataset tiene', filas_blancas, 'filas completamente en blanco.'))
    # El dataset tiene 11 filas completamente en blanco.

    datos_limpios <- datos[!apply(datos, 1, function(x) all(is.na(x) | x == "")), ]
    #num_filas <- nrow(datos_limpios)
    #print(paste('El dataset ahora tiene', num_filas, 'filas después de eliminar las filas en blanco.'))
    # El dataset ahora tiene 127255 filas después de eliminar las filas en blanco.

    datos_repetidos <- datos_limpios %>% group_by_all() %>% tally() %>% filter(n > 1)

    #print(paste('El dataset tiene', nrow(datos_repetidos), 'filas repetidas.'))
    #El dataset tiene 6462 filas repetidas.

    Repetidos_seleccionados <- datos_repetidos %>% select(1, 2, n)

    # Mostrar el resultado
    View(Repetidos_seleccionados)


    frecuencias_familia <- table(datos_limpios$Familia)
    print(frecuencias_familia)
    hist(frecuencias_familia, 
     breaks = "Sturges", 
     col = "blue", 
     xlab = "Cantidad", 
     ylab = "Frecuencia", 
     main = "Distribución de Cantidad de Llantas Vendidas (Regla de Sturges)")


frecuencias_familia <- table(datos_limpios$Familia)
    frecuencias <- as.vector(frecuencias_familia)
    etiquetas <- names(frecuencias_familia)
}

    # GRÁFICA 2: ---------------------------------------------------
    datos_limpios$Fecha <- as.Date(datos_limpios$Fecha, format = "%d/%m/%Y")
    datos_limpios$AnioVenta <- format(datos_limpios$Fecha, "%Y")
    datos_limpios$AnioVenta <- as.numeric(as.character(datos_limpios$AnioVenta))

    datos_limpios$NombreEmpleado <- paste("Empleado", datos_limpios$Empleado)

    anos_unicos <- unique(datos_limpios$AnioVenta)
    empleados_unicos <- unique(datos_limpios$NombreEmpleado)

    View(empleados_unicos)

     ventas_por_empleado_anio <- aggregate(Ventas ~ NombreEmpleado + AnioVenta, data = datos_limpios, FUN = sum)

# Todos los empleados ------------------------------------
    empleados <- unique(ventas_por_empleado_anio$NombreEmpleado)
    anos <- unique(ventas_por_empleado_anio$AnioVenta)
    ventas_matrix <- matrix(0, nrow = length(anos), ncol = length(empleados))
    colnames(ventas_matrix) <- empleados
    rownames(ventas_matrix) <- anos

    for (empleado in empleados) {
    for (anio in anos) {
        ventas <- ventas_por_empleado_anio$Ventas[ventas_por_empleado_anio$NombreEmpleado == empleado & ventas_por_empleado_anio$AnioVenta == anio]
        if (length(ventas) > 0) {
        ventas_matrix[as.character(anio), empleado] <- ventas
        }
    }
    }

    plot(anos, ventas_matrix[,1], type = "l", col = 1, lwd = 2, 
        xlab = "Año", ylab = "Número de Ventas", 
        main = "Número de Ventas por Empleado en Diferentes Años")


    for (i in 2:ncol(ventas_matrix)) {
    lines(anos, ventas_matrix[,i], col = i, lwd = 2)
    }

    legend("topright", legend = colnames(ventas_matrix), col = 1:ncol(ventas_matrix), lty = 1, lwd = 2, title = "Empleados")


# los 10 Empleados: -------------------------------------------

ventas_por_empleado_anio <- aggregate(Ventas ~ NombreEmpleado + AnioVenta, data = datos_limpios, FUN = sum)

total_ventas_por_empleado <- aggregate(Ventas ~ NombreEmpleado, data = datos_limpios, FUN = sum)

top_10_empleados <- total_ventas_por_empleado[order(-total_ventas_por_empleado$Ventas), ][1:10, "NombreEmpleado"]

ventas_top_10 <- subset(ventas_por_empleado_anio, NombreEmpleado %in% top_10_empleados)

anos <- unique(ventas_top_10$AnioVenta)
ventas_matrix <- matrix(0, nrow = length(anos), ncol = length(top_10_empleados))
colnames(ventas_matrix) <- top_10_empleados
rownames(ventas_matrix) <- anos

for (empleado in top_10_empleados) {
  for (anio in anos) {
    ventas <- ventas_top_10$Ventas[ventas_top_10$NombreEmpleado == empleado & ventas_top_10$AnioVenta == anio]
    if (length(ventas) > 0) {
      ventas_matrix[as.character(anio), empleado] <- ventas
    }
  }
}

plot(anos, ventas_matrix[,1], type = "l", col = 1, lwd = 2, 
     xlab = "Año", ylab = "Número de Ventas", 
     main = "Número de Ventas por los 10 Principales Empleados en Diferentes Años")

for (i in 2:ncol(ventas_matrix)) {
  lines(anos, ventas_matrix[,i], col = i, lwd = 2)
}

legend("topright", legend = colnames(ventas_matrix), col = 1:ncol(ventas_matrix), lty = 1, lwd = 2, title = "Empleados")


# OTRO INTENTO
# Imprimir los conteos por empleado
plot(anos_unicos, conteos_por_empleado[[empleados_unicos[1]]], type = "l", col = 1, lwd = 2,
     xlab = "Año", ylab = "Número de Ventas",
     main = "Número de Ventas por Empleado en Diferentes Años")

# Paso 2: Añadir líneas para los otros empleados
for (i in 2:length(empleados_unicos)) {
  lines(anos_unicos, conteos_por_empleado[[empleados_unicos[i]]], col = i, lwd = 2)
}

# Paso 3: Añadir la leyenda
legend("topright", legend = empleados_unicos, col = 1:length(empleados_unicos), lty = 1, lwd = 2, title = "Empleados")

main()