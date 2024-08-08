# Graficos estadisticos: Eduardo Mendieta, Freddy Montalván.


main <- function(){
   
    par(mfrow = c(3, 1))

    # EJERCICIO 1: -------------------------------
    colores_cabello <- c('Rubio', 'Pelirrojo', 'Moreno')
    frecuencias <- c(6, 4, 14)
    barplot(height = frecuencias, names = colores_cabello, space = 1, width = 2, col = '#DA093C', xlab = 'Color de cabello', ylab = 'Frecuencia', ylim = c(0, 14))
    grid(col = '#1B060B', lty = 'dotted')

    # EJERCICIO 2: -------------------------------
    escalas <- c('Insuficiente', 'Suficiente', 'Bien', 'Notable', 'Sobresaliente')
    frecuencias <- c(3, 5, 11, 6, 4)
    barplot(height = frecuencias, names = escalas, space = 1, col = '#DA093C', ylab = 'Frecuencia', ylim = c(0, 14))
    grid(col = '#1B060B', lty = 'dotted')

    # EJERCICIO 3: -------------------------------
    frecuencias <- c(3, 24, 30, 21, 12)    
    libros <- c('Poesía', 'Terror', 'Aventuras', 'Misterio', 'Teatro')
    pie(frecuencias, labels = libros, col = topo.colors(5), cex = 2)
}


main()
