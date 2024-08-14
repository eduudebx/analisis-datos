# Gráfica de líneas: ------------------------------------------------------------------- 

valores_x <- 1:100
valores_y <- cumsum(rnorm(100))
valores_y_2 <- cumsum(rnorm(100))

plot(valores_x, valores_y, main = 'Grafica de lineas', xlab = 'Escala', ylab = 'Valores', type = 'l', col = 'red')
lines(valores_x, valores_y_2, col = 'blue', lwd = 2)
legend('topleft', legend = c('TDS', 'TSBD'), col = c('blue', 'red'), lty = 1)


# Gráfico de calor: --------------------------------------------------------------------

datos <- matrix(rnorm(100), nrow = 10, ncol = 10)

heatmap(datos, main = 'Gráfico de calor', col = heat.colors(10), scale = 'column')
