from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import sqlite3
from tkinter import ttk

def cerrar_ventana():
    ventana.destroy()

def ordenar_por_edad():
    items = [(tree.set(item, "edad"), item) for item in tree.get_children("")]
    items.sort(reverse=True)
    for index, (_, item) in enumerate(items):
        tree.move(item, "", index)

def filtrar_por_talleres(event):
    selected_taller = combo_talleres.get()
    tree.delete(*tree.get_children())
    
    conn = sqlite3.connect("presos.db")
    cursor = conn.cursor()
    
    if selected_taller == "Todos los talleres":
        cursor.execute("SELECT * FROM presos")
    else:
        cursor.execute("SELECT * FROM presos WHERE talleres LIKE ?", ('%' + selected_taller + '%',))
    
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", END, text="", values=row)
    
    conn.close()

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Visualizar Presos")
ventana.geometry("1360x760")

imagen_fondo = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1360, 760), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)
# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear el Treeview
tree = ttk.Treeview(ventana)
tree["columns"] = ("nombres", "apellidos", "tipo_documento", "documento", "fecha_nacimiento", "edad", "tiempo_condena", "pena", "conducta", "talleres")

# Configurar las columnas del Treeview
tree.column("#0", width=0, stretch=NO)
tree.column("nombres", anchor=W, width=150)
tree.column("apellidos", anchor=W, width=150)
tree.column("tipo_documento", anchor=W, width=150)
tree.column("documento", anchor=W, width=150)
tree.column("fecha_nacimiento", anchor=W, width=150)
tree.column("edad", anchor=W, width=150)
tree.column("tiempo_condena", anchor=W, width=150)
tree.column("pena", anchor=W, width=150)
tree.column("conducta", anchor=W, width=150)
tree.column("talleres", anchor=W, width=150)

# Configurar los encabezados de las columnas
tree.heading("#0", text="")
tree.heading("nombres", text="Nombres")
tree.heading("apellidos", text="Apellidos")
tree.heading("tipo_documento", text="Tipo de Documento")
tree.heading("documento", text="Documento")
tree.heading("fecha_nacimiento", text="Fecha de Nacimiento")
tree.heading("edad", text="Edad", command=ordenar_por_edad)  # Agregar comando para ordenar por edad
tree.heading("tiempo_condena", text="Tiempo de Condena")
tree.heading("pena", text="Pena")
tree.heading("conducta", text="Conducta")
tree.heading("talleres", text="Talleres")

# Obtener los presos de la base de datos
conn = sqlite3.connect("presos.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM presos")
rows = cursor.fetchall()

# Insertar los presos en el Treeview
for row in rows:
    tree.insert("", END, text="", values=row)

conn.close()

# Colocar el Treeview en un Scrollbar
scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
tree.pack()

# Combobox de talleres
combo_talleres = ttk.Combobox(ventana, state="readonly")
combo_talleres["values"] = ["Todos los talleres", "Mecánica", "Orfebrería", "Cocina", "Otros"]
combo_talleres.current(0)
combo_talleres.bind("<<ComboboxSelected>>", filtrar_por_talleres)
combo_talleres.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()