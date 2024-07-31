# Tablas de Frecuencias: -----------------------------------------------

edades <- c(38,15,10,12,62,46,25,56,27,24,23,21,20,25,38,27,48,35,50,65,
            59,58,47,42,37,35,32,40,28,14,12,24,66,73,72,70,68,65,54,48,
            34,33,21,19,64,59,47,46,30,30)

minimo <- min(edades)
maximo <- max(edades)
longitud <- length(edades)
num_intervalos_v1 <- sqrt(longitud)
num_intervalos_v2 <- nclass.Sturges(edades)
amplitud <- (maximo - minimo) / num_intervalos_v2
extremos <- minimo + amplitud * (0: num_intervalos_v2)
extremo_inf <- minimo + amplitud * (0: (num_intervalos_v2 - 1))
extremo_sup <- minimo + amplitud * (1: num_intervalos_v2)
marca_clase <- (extremo_inf + extremo_sup) / 2

tabla_frecuencias <- function(x, y){ 
    cut1 <- cut(x, breaks = y, right = FALSE, include.loweat = b)
    intervalos <- levels(cut1)
    frecuencia_abs <- as.vector(table(cut1))
    frecuencia_rel <- round(frecuencia_abs / longitud, digits = 2)
    frecuencia_abs_acum <- cumsum(frecuencia_abs)
    frecuencia_rel_acum <- cumsum(frecuencia_rel)
    tabla <- data.frame(intervalos, marca_clase, frecuencia_abs, frecuencia_abs_acum, frecuencia_rel, frecuencia_rel_acum)
}

tabla_resultante <- tabla_frecuencias(x = edades, y = extremos)
View(tabla_resultante)



