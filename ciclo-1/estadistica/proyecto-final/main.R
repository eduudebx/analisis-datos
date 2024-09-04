library(readxl)


# OPERACIONES -------------------------------------------------------------------------------
obtener_coincidencias <- function(set_datos, nombre_columna){
    columna <- set_datos[[nombre_columna]]
    conteo <- as.data.frame(table(columna))
    etiquetas <- as.vector(conteo[, 1])
    coincidencias <- as.vector(conteo[, 2])
    return(list(etiquetas = etiquetas, num_coincidencias = coincidencias))
}


gen_tbl_frecuencias_acum <- function(set_datos, nombre_columna, etiqueta_columna, ver_tabla){
    datos <- as.vector(set_datos[[nombre_columna]])
    
    num_datos <- length(datos)
    minimo <- min(datos)
    maximo <- max(datos)
    clases <- nclass.Sturges(datos)
    amplitud <- ceiling((maximo - minimo) / clases)

    extremos <- minimo + amplitud * (0: clases)
    
    if(ver_tabla){
        extremo_inferior <- minimo + amplitud * (0: (clases - 1))
        extremo_superior <- minimo + amplitud * (1: clases)
        marca_clase <- (extremo_inferior + extremo_superior) / 2
        
        factor <- cut(datos, breaks = extremos, right = FALSE, include.lowest = TRUE)
        intervalos <- levels(factor)

        frecuencia_absoluta <- as.vector(table(factor))
        frecuencia_relativa <- round(frecuencia_absoluta / num_datos, digits = 2)
        frecuencia_absoluta_acum <- cumsum(frecuencia_absoluta)
        frecuencia_relativa_acum <- cumsum(frecuencia_relativa)
        frecuencia_porcentual <- paste(round(frecuencia_relativa * 100, digits = 2), '%')

        print(paste('n =', num_datos, '| Min =', minimo, '| Max =', maximo))
        print(paste('k =', clases, '| a =', amplitud))

        tabla <- data.frame(intervalos, marca_clase, frecuencia_absoluta, frecuencia_absoluta_acum, 
                            frecuencia_relativa, frecuencia_relativa_acum, frecuencia_porcentual)

        colnames(tabla) <- c(etiqueta_columna, 'Marca de Clase', 'Frecuencia Absoluta', 'Frecuencia Absoluta Acumulada', 
                            'Frecuencia Relativa', 'Frecuencia Relativa Acumulada', 'Frecuencia Porcentual')

        View(tabla)
    }

    return(list(datos = datos, extremos = extremos))
}


gen_tbl_frecuencias <- function(set_datos, nombre_columna, etiqueta_columna){
    datos_frecuecias <- obtener_coincidencias(set_datos, nombre_columna)
    tabla <- data.frame(datos_frecuecias$etiquetas, datos_frecuecias$num_coincidencias)
    colnames(tabla) <- c(etiqueta_columna, 'Frecuencias')
    View(tabla)
}


# VISUALIZACIÓN -----------------------------------------------------------------------------
gen_histograma <- function(){
    
}


# PRINCIPAL ---------------------------------------------------------------------------------
main <- function(){
    set_datos <- read_excel('datos.xlsx')

    #gen_tbl_frecuencias_acum(set_datos, 'Edad', 'Edades')
    #gen_tbl_frecuencias_acum(set_datos, 'Horas_Suenio_Sem', 'Horas de sueño')
    #gen_tbl_frecuencias_acum(set_datos, 'Horas_Estudio_Sem', 'Horas de estudio')
    #gen_tbl_frecuencias_acum(set_datos, 'Horas_Diarias_Redes', 'Horas en redes')

    #gen_tbl_frecuencias(set_datos, 'Nivel_Previo', 'Nivel de instrucción previa')
}


main()