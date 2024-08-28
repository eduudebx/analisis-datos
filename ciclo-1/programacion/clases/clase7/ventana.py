import tkinter as tk
import sqlite3
from tkinter import messagebox


def init_db():
    conn = sqlite3.connect('persona.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS persona(
                   id INTEGER PRIMARY KEY, 
                   cedula TEXT,
                   nombre TEXT, 
                   direccion TEXT,
                   telefono TEXT,
                   correo TEXT,
                   usuario TEXT,
                   clave TEXT)''')
    conn.commit()
    conn.close()


def guardar_datos():
    cedula = txt_cedula.get()
    nombre = txt_nombre.get()
    direccion = txt_direccion.get()
    telefono = txt_telefono.get()
    correo = txt_correo.get()
    usuario = txt_usuario.get()
    clave = txt_clave.get()

    if cedula and nombre and direccion and telefono and correo and usuario and clave:
        conn = sqlite3.connect('persona.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO persona (cedula ,nombre, direccion, telefono, correo, usuario, clave) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       (cedula, nombre, direccion, telefono, correo, usuario, clave))
        conn.commit()
        conn.close()
        messagebox.showinfo("Información", "Datos guardados exitosamente!")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos!")


ventana = tk.Tk()
ventana.title("Ventana de registro")


tk.Label(ventana, text="Cédula:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(ventana, text="Nombre y apellido:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(ventana, text="Dirección:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(ventana, text="Teléfono:").grid(row=3, column=0, padx=10, pady=10)
tk.Label(ventana, text="Correo:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(ventana, text="Nombre de usuario:").grid(row=5, column=0, padx=10, pady=10)
tk.Label(ventana, text="Clave:").grid(row=6, column=0, padx=10, pady=10)


txt_cedula =  tk.Entry(ventana)
txt_nombre =  tk.Entry(ventana)
txt_direccion =  tk.Entry(ventana)
txt_telefono =  tk.Entry(ventana)
txt_correo =  tk.Entry(ventana)
txt_usuario =  tk.Entry(ventana)
txt_clave =  tk.Entry(ventana, show="*")


txt_cedula.grid(row=0, column=1, padx=10, pady=10)
txt_nombre.grid(row=1, column=1, padx=10, pady=10)
txt_direccion.grid(row=2, column=1, padx=10, pady=10)
txt_telefono.grid(row=3, column=1, padx=10, pady=10)
txt_correo.grid(row=4, column=1, padx=10, pady=10)
txt_usuario.grid(row=5, column=1, padx=10, pady=10)
txt_clave.grid(row=6, column=1, padx=10, pady=10)

tk.Button(ventana,text="Aceptar",command=guardar_datos).grid(row=7, column=1, padx=10, pady=10)


init_db()
ventana.mainloop()