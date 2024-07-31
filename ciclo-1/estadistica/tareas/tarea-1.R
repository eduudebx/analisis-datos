# Integrantes: Eduardo Mendieta, Juan Orellana.

get_tbl_frecuencias <- function(data, extremos, marca_clase){
    factor <- cut(data, breaks = extremos, right = FALSE, include.lowest = TRUE)
    intervalos <- levels(factor)

    frec_abs <- as.vector(table(factor))
    frec_rel <- round(frec_abs / length(data), digits = 2)
    frec_abs_acum <- cumsum(frec_abs)
    frec_rel_acum <- cumsum(frec_rel)

    tabla <- data.frame(intervalos, marca_clase, frec_abs, frec_abs_acum, frec_rel, frec_rel_acum)
}


histograma <- function (data, extremos, titulo, xlab, ylab, col_barras, col_grid){
    hist(data, main = titulo, ylab = ylab, xlab = xlab, col = col_barras, include.lowest = TRUE, right = FALSE, breaks = extremos)
    grid(nx = NA, ny = NULL, lty = 2, col = col_grid, lwd = 2)
}


main <- function(){
    edades <- c(38,15,10,12,62,46,25,56,27,24,23,21,20,25,38,27,48,35,50,65,59,58,47,42,37,
                35,32,40,28,14,12,24,66,73,72,70,68,65,54,48,34,33,21,19,64,59,47,46,30,30)
    
    n <- length(edades)
    minimo <- min(edades)
    maximo <- max(edades)
    clases <- nclass.Sturges(edades)
    amplitud <- (maximo - minimo) / clases

    extremos <- minimo + amplitud * (0: clases)
    extremo_inf <- minimo + amplitud * (0: (clases - 1))
    extremo_sup <- minimo + amplitud * (1: clases)

    marca_clase <- (extremo_inf + extremo_sup) / 2

    tabla_resultante <- get_tbl_frecuencias(data = edades, extremos = extremos, marca_clase = marca_clase)

    View(tabla_resultante)

    histograma(data = edades, extremos = extremos, 
               titulo = 'Histograma de Frecuencias', xlab = 'Edades', ylab = 'Frecuencias', 
               col_barras = '#00C1FF', col_grid = '#FF336E')
}


main()