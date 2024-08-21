# Funciones: -----------------------------------------------------------

import clase6


clase6.saludar('Juanito', 18)
clase6.saludar('Chanchito', 20)

nombre, edad = clase6.pedir_datos()
clase6.saludar(nombre, edad)

numeros = clase6.solicitar_enteros(2)
clase6.dividir(numeros[0], numeros[1])