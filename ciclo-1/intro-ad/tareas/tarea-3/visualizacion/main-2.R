library(readxl)


grafica1 <- function(datos_limpios){

    par(mfrow = c(2, 3))

    anios <- unique(datos_limpios$AnioVenta)

    for(anio in anios){
        datos_filtrados <- datos_limpios[datos_limpios$AnioVenta == anio, ]
        nombres_unicos <- sort(unique(datos_filtrados$NombreEmpleado))

        ventas_empleados <- vector('numeric')
        for (nombre in nombres_unicos) {
            filtro <- datos_limpios[datos_limpios$NombreEmpleado == nombre, ]
            ventas_empleados <- c(ventas_empleados, length(filtro$Ventas))
        }

        barplot(height = ventas_empleados, names = nombres_unicos, horiz = 1,  las = 1,
                main = paste('Total de ventas por empleado en el año', anio))
        grid(col = '#2B434F')
    }
}



main <- function(){
    datos_limpios <- read_excel('datos-limpios.xlsx')

    datos_limpios$Fecha <- as.Date(datos_limpios$Fecha, format = "%d/%m/%Y")
    datos_limpios$AnioVenta <- format(datos_limpios$Fecha, "%Y")
    datos_limpios$NombreEmpleado <- paste("Emp", datos_limpios$Empleado)

    datos_limpios$AnioVenta <- as.numeric(as.character(datos_limpios$AnioVenta))

    grafica1(datos_limpios)
}

main()