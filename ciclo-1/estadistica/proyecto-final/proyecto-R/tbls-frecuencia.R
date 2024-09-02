library(readxl)


get_datos <- function(){
    return(read_excel('datos-limpios.xlsx'))
}


get_frecuencias <- function(datos, col_name){
    etiquetas <- unique(datos[[col_name]])
    frecuencias <- c()

    etiquetas <- sort(unlist(etiquetas))

    for (i in etiquetas){
        num_datos <- sum(datos[[col_name]] == i)
        frecuencias <- append(frecuencias, num_datos)
    }

    return(list(etiquetas = etiquetas, frecuencias = frecuencias))
}

get_frecuencias_1 <- function(datos, col_name){
    etiquetas <- unique(datos[[col_name]])
    frecuencias <- sapply(etiquetas, function(x) sum(datos == x))
    return(list(etiquetas = etiquetas, frecuencias = frecuencias))
}

gen_tbls_frecuancias_acum <- function(datos, col_name, lbl_name){
    n <- length(datos[[col_name]])
    frecuencias <- get_frecuencias(datos, col_name)

    etiquetas <- frecuencias$etiquetas
    frecuencia_abs <- frecuencias$frecuencias
    frecuencia_abs_acum <- cumsum(frecuencia_abs)
    frecuencia_rel <- unlist(lapply(frecuencia_abs, function(x) round(x / n, 2)))
    frecuencia_rel_acum <- cumsum(frecuencia_rel)
    frecuencia_porcentual <- unlist(lapply(frecuencia_rel, function(x) paste(round(x * 100, 2), '%')))
    tabla <- data.frame(etiquetas, frecuencia_abs, frecuencia_abs_acum, frecuencia_rel, frecuencia_rel_acum, frecuencia_porcentual)
    colnames(tabla) <- c(lbl_name, 'Frecuencia Absoluta', 'Frecuencia Absoluta Acumulada', 
                         'Frecuencia Relativa', 'Frecuencia Relativa Acumulada', 'Frecuancia Porcentual')
    return(tabla)
}

gen_tbls_frecuancias <- function(datos, col_name, col1_name, col2_name){
    n <- length(datos[[col_name]])
    frecuencias <- get_frecuencias(datos, col_name)

    etiquetas <- frecuencias$etiquetas
    frecuencia_abs <- frecuencias$frecuencias

    tabla <- data.frame(etiquetas, frecuencia_abs)
    colnames(tabla) <- c(col1_name, col2_name)

    return(tabla)
}


main <- function(){
    datos <- get_datos()

    #print(sum(is.na(datos$Horas_Suenio)))
    View(gen_tbls_frecuancias_acum(datos, 'Horas_Estudio_Sem', 'Horas de Estudio a la semana'))
}


main()