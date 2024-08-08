# Gráficos de Pastel: -----------------------------------------------------
library(RColorBrewer)


main <- function(){
    datos <- c(12, 37, 6, 33, 3, 54)

    par(mfrow = c(2, 3))

    pie(datos)
    pie(datos, labels = paste0(datos, '%'))
    pie(datos, labels = datos, col = 1:6, cex = 2)
    pie(datos, labels = datos, col = rainbow(6), cex = 2)
    pie(datos, labels = datos, col = topo.colors(6), cex = 2)

    color <- brewer.pal(length(datos), 'Set2')
    pie(datos, labels = datos, col = color, lty = 2)
}


main()
