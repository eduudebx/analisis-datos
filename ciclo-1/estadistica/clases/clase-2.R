# Histogramas --------------------------------------------------

distancias <- c(228, 259, 245, 277, 291, 235, 283, 247, 272, 266,
               252, 296, 229, 260, 248, 273, 282, 254, 290, 245,
               279, 224, 267, 294, 233, 258, 280, 231, 275, 287,
               240, 270, 244, 296, 230, 264, 292, 253, 278, 261,
               250, 285, 239, 288, 274, 232, 255, 297, 268, 245,
               293, 220, 284, 249, 271, 256, 290, 246, 259, 278,
               262, 285, 272, 294, 227, 241, 286, 237, 277, 288,
               265, 293, 244, 295, 234, 273, 260, 284, 220, 297)

par(mfrow = c(1, 3))

hist(distancias, main = 'Histograma de ejemplo 1', ylab = 'Frecuencias', xlab = 'Distancias', col = '#33FFC7', breaks = 6)
grid(nx = NA, ny = NULL, lty = 2, col = '#FF336E', lwd = 2)

hist(distancias, main = 'Histograma de ejemplo 2', ylab = 'Frecuencias', xlab = 'Distancias', col = '#3390FF', breaks = 20)
grid(nx = NA, ny = NULL, lty = 2, col = '#FF336E', lwd = 2)

hist(distancias, main = 'Histograma de ejemplo 3', ylab = 'Frecuencias', xlab = 'Distancias', col = '#8633FF', breaks = 40)
grid(nx = NA, ny = NULL, lty = 2, col = '#FF336E', lwd = 2)
