import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as db



# Comunicación con la base de datos: --------------------------------------------------------
def init_db():
    conn = db.connect('mascotas.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mascota(
                   id INTEGER PRIMARY KEY,
                   ruta_foto TEXT,
                   nombre TEXT,
                   apellido TEXT,
                   estatura REAL,
                   peso REAL,
                   fecha_nacimiento TEXT,
                   raza TEXT,
                   sexo TEXT)''')
    conn.commit()
    conn.close()




# Ventana principal: ------------------------------------------------------------------------
ventana = tk.Tk()
ventana.title('Registro de mascotas')
ventana.geometry('580x300')


# Etiquetas: --------------------------------------------------------------------------------
lbl_id = tk.Label(ventana, text='id:', padx=5, pady=10)
lbl_foto = tk.Label(ventana, text='Foto:', padx=5, pady=10)
lbl_nombre = tk.Label(ventana, text='Nombre:', padx=5, pady=10)
lbl_apellido = tk.Label(ventana, text='Apellido:', padx=5, pady=10)
lbl_estatura = tk.Label(ventana, text='Estatura:', padx=5, pady=10)
lbl_peso = tk.Label(ventana, text='Peso:', padx=5, pady=10)
lbl_fecha_nac = tk.Label(ventana, text='Fecha de Nacimiento:', padx=5, pady=10)
lbl_raza = tk.Label(ventana, text='Raza:', padx=5, pady=10)
lbl_sexo = tk.Label(ventana, text='Sexo:', padx=5, pady=10)

lbl_id.grid(column = 0, row = 0)
lbl_foto.grid(column = 2, row = 0)
lbl_nombre.grid(column = 0, row = 1)
lbl_apellido.grid(column = 2, row = 1)
lbl_estatura.grid(column = 0, row = 2)
lbl_peso.grid(column = 2, row = 2)
lbl_fecha_nac.grid(column = 0, row = 3)
lbl_raza.grid(column = 2, row = 3)
lbl_sexo.grid(column = 0, row = 4)


# Selector de imagen: -----------------------------------------------------------------------
#foto = tk.PhotoImage(file='perro.png')
#lbl_foto_mascota = ttk.Label(ventana, image=foto)
#lbl_foto_mascota.grid(column = 3, row = 0)


# Cajas de texto: ---------------------------------------------------------------------------
txt_id = ttk.Entry(ventana)
txt_nombre = ttk.Entry(ventana)
txt_apellido = ttk.Entry(ventana)
txt_estatura = ttk.Entry(ventana)
txt_peso = ttk.Entry(ventana)
txt_fecha_nac = ttk.Entry(ventana)

txt_id.grid(column=1, row=0)
txt_nombre.grid(column=1, row=1)
txt_apellido.grid(column=3, row=1)
txt_estatura.grid(column=1, row=2)
txt_peso.grid(column=3, row=2)
txt_fecha_nac.grid(column=1, row=3)


# Combobox: ---------------------------------------------------------------------------------
combo_raza = ttk.Combobox(ventana, 
                          values=['Mestizo', 'Labrador Retriever', 'Pastor Alemán', 
                                  'Bulldog Inglés', 'Poodle', 'Beagle', 'Golden Retriever', 
                                  'Rottweiler', 'Chihuahua', 'Dachshund', 'Otro'])
combo_raza.set('Mestizo')

combo_raza.grid(column=3, row=3)


# Botones de radio: ----------------------------------------------------------------------------
rbtn_sexo_selec = tk.IntVar(value=1)
rbtn_hembra = tk.Radiobutton(ventana, text='Hembra', variable=rbtn_sexo_selec, value=1)
rbtn_macho = tk.Radiobutton(ventana, text='Macho', variable=rbtn_sexo_selec, value=2)

rbtn_hembra.grid(column=1, row=4)
rbtn_macho.grid(column=2, row=4)


# Botones: ----------------------------------------------------------------------------------
def registrar_mascota():
    
    url_foto = ''
    nombre = txt_nombre.get()
    apellido = txt_apellido.get()
    estatura = float(txt_estatura.get()) if txt_estatura.get() != '' else 0
    peso = float(txt_peso.get()) if txt_peso.get() != '' else 0
    fecha_nac = txt_fecha_nac.get()
    raza = combo_raza.get()
    sexo = 'Hembra' if rbtn_sexo_selec.get() == 1 else 'Macho'

    if nombre and apellido and estatura and peso and fecha_nac and raza and sexo:
        conn = db.connect('mascotas.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mascota(ruta_foto, nombre, apellido, estatura, peso, fecha_nacimiento, raza, sexo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (url_foto, nombre, apellido, estatura, peso, fecha_nac, raza, sexo))
        conn.commit()
        conn.close()
        messagebox.showinfo('Info', 'Guardado exitosamente!')
    else:
        messagebox.showwarning('Advertencia', 'Debe completar todos los campos!')


btn_registrar = tk.Button(ventana, text='Registrar', command=registrar_mascota, pady=5)
btn_salir = tk.Button(ventana, text='Salir', command=ventana.destroy, pady=5)

btn_registrar.grid(column=1, row=5)
btn_salir.grid(column=2, row=5)


# Ejecución de la ventana: ------------------------------------------------------------------
init_db()
ventana.mainloop()
