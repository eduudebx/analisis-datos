library(readxl)
library(dplyr)
library(stringr)
library(openxlsx)
library(RColorBrewer)
library(plotrix)


limpiar <- function(){
       
    datos <- read_excel('ds-ventallantas-original.xlsx')
    datos_limpios <- datos[!apply(datos, 1, function(x) all(is.na(x) | x == "")), ]

    datos_limpios <- datos_limpios %>% arrange(Empleado)
    datos_limpios <- datos_limpios[!duplicated(datos_limpios) & !duplicated(datos_limpios, fromLast = TRUE), ]

    datos_limpios$Empleado <- as.numeric(datos_limpios$Empleado) 
    datos_limpios$CodigoFamilia <- as.numeric(datos_limpios$CodigoFamilia)
    datos_limpios$Ventas <- as.numeric(datos_limpios$Ventas)
    datos_limpios$Area <- as.numeric(datos_limpios$Area)
    datos_limpios$Cantidad <- as.numeric(datos_limpios$Cantidad)

    datos_limpios$Cantidad <- ifelse(datos_limpios$Cantidad != floor(datos_limpios$Cantidad), 
                                    ceiling(datos_limpios$Cantidad), 
                                    datos_limpios$Cantidad)

    datos_limpios$Fecha <- format(as.Date(datos_limpios$Fecha, format = "%m/%d/%Y"), "%d/%m/%Y")


    datos_limpios <- datos_limpios %>%
        mutate(
            NombreCliente = str_to_title(NombreCliente),
            Descripcion = str_to_title(Descripcion),
            Familia = str_to_title(Familia),
            Localidad = str_to_title(Localidad),
            Sede = str_to_title(Sede)
        )

    write.xlsx(datos_limpios, 'datos-limpios.xlsx')
}


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


grafica2 <- function(datos_limpios){

    categorias <- unique(datos_limpios$Familia)
    
    cantidades <- vector('numeric')
    for(categoria in categorias){
        datos_filtrados <- datos_limpios[datos_limpios$Familia == categoria, ]
        cantidades <- c(cantidades, length(datos_filtrados$Familia))
    }
    porcentajes <- round(cantidades / sum(cantidades) * 100, 1)
    pie3D(cantidades, labels = paste(categorias, porcentajes, '%', sep=' '), explode = 0.1, 
          main = 'Porcentaje de categorias vendidas')
}


grafica3 <- function(datos_limpios){
    sedes = unique(datos_limpios$Sede)
    anios = unique(datos_limpios$AnioVenta)

    
}


main <- function(){

    limpiar()

    datos_limpios <- read_excel('datos-limpios.xlsx')

    datos_limpios$Fecha <- as.Date(datos_limpios$Fecha, format = "%d/%m/%Y")
    datos_limpios$AnioVenta <- format(datos_limpios$Fecha, "%Y")
    datos_limpios$NombreEmpleado <- paste("Emp", datos_limpios$Empleado)

    datos_limpios$AnioVenta <- as.numeric(as.character(datos_limpios$AnioVenta))

    grafica1(datos_limpios)
    grafica2(datos_limpios)
    grafica3(datos_limpios)
}


main()