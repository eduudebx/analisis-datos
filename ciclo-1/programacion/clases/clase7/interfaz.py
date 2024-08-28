import tkinter as tk
import sqlite3
from tkinter import messagebox


def init_db():
    print('Iniciando Base de Datos')
    conn = sqlite3.connect('Prueba1.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS persona
                      (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)''')
    conn.commit()
    conn.close()

def guardarDatos():
    nombre = texto_Nombre.get()
    apellido = texto_Apellido.get()

    if nombre and apellido:  # Verificar que los campos no estén vacíos
        conn = sqlite3.connect('Prueba1.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persona (nombre, apellido) VALUES (?, ?)", (nombre, apellido))
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Datos guardados exitosamente")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")

ventana = tk.Tk()
ventana.title("ventana de registro")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10)
texto_Nombre = tk.Entry(ventana)
texto_Nombre.grid(row=0, column=1, padx=10, pady=10)
tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=10)
texto_Apellido = tk.Entry(ventana)
texto_Apellido.grid(row=1, column=1, padx=10, pady=10)
tk.Radiobutton(ventana, text="Hombre").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(ventana, text="Mujer").grid(row=3, column=0, padx=10, pady=10)
tk.Button(ventana,text="Aceptar",command=guardarDatos).grid(row=4, column=1, padx=10, pady=10)



init_db()
ventana.mainloop()
