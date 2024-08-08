# Graficos de barras en R: -----------------------------------------

main <- function(){
    animales  <- c('perro', 'gato', 'tortuga', 'pajaro')
    frecuencias <- c(10, 5, 3, 8)

    par(mfrow = c(2, 2))

    barplot(height = frecuencias, names = animales, col = '#239FFB', ylim = c(0, 12), width = c(1, 1, 3, 1))
    barplot(height = frecuencias, names = animales, col = 'black', main = 'Animales Populares', ylab = 'Frecuencias', xlab = 'Animales')
    barplot(height = frecuencias, names = animales, col = c('#123F3A', '#AF1696', 'white', '#FFF345'), border = 'black', space = 0)
    barplot(height = frecuencias, names = animales, col = 'white', border = 'black', horiz = 1, las = 1)
}


main()
