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


main()