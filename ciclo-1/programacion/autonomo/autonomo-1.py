import tkinter as tk
from tkinter import ttk


# Creacion de una ventana: --------------------------------------------------------
ventana = tk.Tk()
ventana.title('Ventana')
ventana.resizable(0, 0) # Evita modificar el tamaño de una ventana.

# Etiquetas: ----------------------------------------------------------------------
etiqueta = tk.Label(ventana, text = 'Escribe tu nombre:')
etiqueta.grid(column = 0, row = 0)

# Cajas de texto: ----------------------------------------------------------------
nombre = tk.StringVar()
txt_nombre = ttk.Entry(ventana, width = 20, textvariable = nombre)
txt_nombre.grid(column = 1, row = 0)

# Listas desplegables: -----------------------------------------------------------
lenguaje = tk.StringVar()
combo_lenguajes = ttk.Combobox(ventana, width=12, textvariable =  lenguaje)
combo_lenguajes['values'] = ('Python', 'R', 'SQL')
combo_lenguajes.current(0)
combo_lenguajes.grid(column = 0, row = 2)

# Checkbutton: -------------------------------------------------------------------
opcion1 = tk.IntVar()
casilla1 = tk.Checkbutton(ventana, text = 'Leer', variable = opcion1, state = 'disabled')
casilla1.select()
casilla1.grid(column = 0, row = 3)

opcion2 = tk.IntVar()
casilla2 = tk.Checkbutton(ventana, text = 'Redes sociales', variable = opcion2)
casilla2.deselect()
casilla2.grid(column = 1, row = 3)

opcion3 = tk.IntVar()
casilla3 = tk.Checkbutton(ventana, text = 'ver películas', variable = opcion3)
casilla3.select()
casilla3.grid(column = 2, row = 3, sticky = tk.W)

# Radiobutton: -------------------------------------------------------------------
COLOR1 = 'alice blue'
COLOR2 = 'aquamarine'
COLOR3 = 'antique white'

def funcion_radio():
    selector = opcion.get()
    if selector == 1:
        ventana.configure(background =  COLOR1)
    elif selector == 2:
        ventana.configure(background =  COLOR2)
    else:
        ventana.configure(background =  COLOR3)

opcion = tk.IntVar()
radio1 = tk.Radiobutton(ventana, text = COLOR1, variable = opcion, value = 1, command = funcion_radio)
radio1.grid(column = 0, row = 4, sticky = tk.W)

radio2 = tk.Radiobutton(ventana, text = COLOR2, variable = opcion, value = 2, command = funcion_radio)
radio2.grid(column = 1, row = 4, sticky = tk.W)

radio3 = tk.Radiobutton(ventana, text = COLOR3, variable = opcion, value = 3, command = funcion_radio)
radio3.grid(column = 2, row = 4, sticky = tk.W)

# Cajas de texto: ----------------------------------------------------------------
from tkinter import scrolledtext

scrol_ancho = 30
scrol_alto = 3
caja = scrolledtext.ScrolledText(ventana, width = scrol_ancho, height = scrol_alto, wrap = tk.WORD)
caja.grid(column = 0, columnspan = 3)

# Botones: -----------------------------------------------------------------------
def funcion_click():
    etiqueta.configure(foreground = 'green')
    btn.configure(text = 'Hola ' + nombre.get())

btn = ttk.Button(ventana, text = 'Haz click!', command = funcion_click)
btn.grid(column = 0, row = 1)
#btn.configure(state = 'disabled') # Desactivamos el boton.

ventana.mainloop()