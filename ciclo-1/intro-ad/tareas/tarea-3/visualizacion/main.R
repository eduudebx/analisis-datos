library(readxl)
library(dplyr)
library(stringr)
library(openxlsx)

limpieza <- function(){
        # LIMPIEZA: -----------------------------------------------------------------------------
    datos <- read_excel('ds-ventallantas-original.xlsx')
    datos_limpios <- datos[!apply(datos, 1, function(x) all(is.na(x) | x == "")), ]

    datos_limpios <- datos_limpios %>% arrange(Empleado)

    #datos_repetidos <- datos_limpios[duplicated(datos_limpios) | duplicated(datos_limpios, fromLast = TRUE), ]
    #print(paste('Datos repetidos:', nrow(datos_repetidos)))
    # Datos repetidos: 24923.

    #View(datos_repetidos)

    datos_limpios <- datos_limpios[!duplicated(datos_limpios) & !duplicated(datos_limpios, fromLast = TRUE), ]
    #print(paste('El dataset ahora tiene:', nrow(datos_limpios), ', luego de eliminar las filas repetidas.'))
    # El dataset ahora tiene: 102332 , luego de eliminar las filas repetidas.

    #print(colSums(is.na(datos_limpios)))


    # VALIDACIÓN DE DATOS ----------------------------------------------------------------------

    # 1. VALIDANDO COLUMNAS NUMERICAS
    datos_limpios$Empleado <- as.numeric(datos_limpios$Empleado)
    #print(sum(is.na(datos_limpios$Empleado) | datos_limpios$Empleado <= 0 | datos_limpios$Empleado != floor(datos_limpios$Empleado)))
    # Respuesta: 0

    datos_limpios$CodigoFamilia <- as.numeric(datos_limpios$CodigoFamilia)
    #print(sum(is.na(datos_limpios$CodigoFamilia) | datos_limpios$CodigoFamilia <= 0 | datos_limpios$CodigoFamilia != floor(datos_limpios$CodigoFamilia)))
    # Respuesta: 0

    datos_limpios$Ventas <- as.numeric(datos_limpios$Ventas)
    #print(sum(is.na(datos_limpios$Ventas) | datos_limpios$Ventas <= 0 | datos_limpios$Ventas != floor(datos_limpios$Ventas)))
    # Respuesta: 0

    datos_limpios$Area <- as.numeric(datos_limpios$Area)
    #print(sum(is.na(datos_limpios$Area) | datos_limpios$Area <= 0 | datos_limpios$Area != floor(datos_limpios$Area)))
    # Respuesta: 0

    datos_limpios$Cantidad <- as.numeric(datos_limpios$Cantidad)
    #print(sum(is.na(datos_limpios$Cantidad)))# Respuesta: 0
    #print(sum(datos_limpios$Cantidad <= 0)) # Respuesta: 0
    #print(sum(datos_limpios$Cantidad != floor(datos_limpios$Cantidad))) # Respuesta: 2

    #valores_no_enteros <- datos_limpios$Cantidad[datos_limpios$Cantidad != floor(datos_limpios$Cantidad)]
    #print(valores_no_enteros) #  1.068 1.006

    datos_limpios$Cantidad <- ifelse(datos_limpios$Cantidad != floor(datos_limpios$Cantidad), 
                                    ceiling(datos_limpios$Cantidad), 
                                    datos_limpios$Cantidad)


    # VALIDACION DE FECHAS:
    #datos_limpios$Fecha <- as.character(datos_limpios$Fecha)
    #print(sum(!is.na(datos_limpios$Fecha) & !is.na(as.Date(datos_limpios$Fecha, format = "%m/%d/%Y"))))
    #Respuesta: 0

    datos_limpios$Fecha <- format(as.Date(datos_limpios$Fecha, format = "%m/%d/%Y"), "%d/%m/%Y")
    #View(datos_limpios)


    # CORRIGIENDO FORMATOS STRING:

    datos_limpios <- datos_limpios %>%
        mutate(
            NombreCliente = str_to_title(NombreCliente),
            Descripcion = str_to_title(Descripcion),
            Familia = str_to_title(Familia),
            Localidad = str_to_title(Localidad),
            Sede = str_to_title(Sede)
        )

    #View(datos_limpios)


    write.xlsx(datos_limpios, 'datos-limpios.xlsx')
}


main <- function(){
    datos_limpios <- read_excel('datos-limpios.xlsx')
    #print(nrow(datos))

    par(mfrow = c(1, 2))

    frecuencias_familia <- table(datos_limpios$Familia)
    empleado_ventas <- table(datos_limpios$Empleado)

    barplot(frecuencias_familia, 
        col = '#33B8FF', 
        xlab = 'Categoría', 
        ylab = 'Cantidad de ventas', 
        main = 'Ventas por categoría de producto', 
        las = 1)
    grid(nx = NA, ny = NULL, lty = 2, col = '#1B060B', lwd = 2)

    
    plot(empleado_ventas, 
     type = "l", 
     col = 'blue', 
     xlab = 'Empleado', 
     ylab = 'Cantidad de vendida', 
     main = 'Ventas por Empleado')
    grid(nx = NA, ny = NULL, lty = 2, col = '#1B060B', lwd = 2)
}


main()