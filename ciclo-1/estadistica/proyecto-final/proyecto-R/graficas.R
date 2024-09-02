library(readxl)
library(ggplot2)
library(plotrix)


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


gen_grafico_barras <- function(datos, col_name, titulo, xlab, ylab, color){
    frecuencias <- get_frecuencias(datos, col_name)

    datos_bar <- data.frame(etiquetas = frecuencias$etiquetas, frecuencias = frecuencias$frecuencias)

    ggplot(datos_bar, aes(x = etiquetas, y = frecuencias)) +
    geom_bar(stat = 'identity', fill = color) +
    xlab(xlab) +
    ylab(ylab) +
    ggtitle(titulo) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}


gen_grafico_pastel <- function(datos, col_name, titulo){
    frecuencias <- get_frecuencias(datos, col_name)
    pie3D(frecuencias$frecuencias,labels = frecuencias$etiquetas, main = titulo)
}


main <- function(){
    datos <- get_datos()
    #gen_grafico_barras(datos = datos, col_name = '', titulo = '', xlab = '', ylab = '', color = '')
    gen_grafico_pastel(datos = datos, col_name = 'Ciclo', 'Ciclos')
}


main()