import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Ventana')
ventana.resizable(0, 0)

# Titulo: ------------------------------------------------
lbl_titulo = tk.Label(ventana, text = 'Registro Personas')
lbl_titulo.grid(column = 0, row = 0)

# Nombre: ------------------------------------------------
lbl_nombre = tk.Label(ventana, text = 'Nombre: ')
lbl_nombre.grid(column = 0, row = 1)
nombre = tk.StringVar()
txt_nombre = ttk.Entry(ventana, width = 20, textvariable = nombre)
txt_nombre.grid(column = 1, row = 1)

# Apellido: ---------------------------------------------
lbl_apellido = tk.Label(ventana, text = 'Apellido')
lbl_apellido.grid(column = 0, row = 2)
apellido = tk.StringVar()
txt_apellido = ttk.Entry(ventana, width = 20, textvariable = apellido)
txt_apellido.grid(column = 1, row = 2)

# Acción: ----------------------------------------------
def decir_nombre():
    print(f'\nHola {nombre.get()} {apellido.get()} como estas!\n')

btn = ttk.Button(ventana, text = 'Aceptar', command = decir_nombre)
btn.grid(column = 0, row = 3)


ventana.mainloop()




