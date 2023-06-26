from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

def mostrar_reclusos():
    # Crear tabla para mostrar los códigos de recluso, nombres y apellidos
    tabla_reclusos = ttk.Treeview(frame_izquierdo, columns=("Código", "Nombre", "Apellido"), show="headings")
    tabla_reclusos.heading("Código", text="Código de Recluso", anchor="center")
    tabla_reclusos.heading("Nombre", text="Nombre del Recluso", anchor="center")
    tabla_reclusos.heading("Apellido", text="Apellido del Recluso", anchor="center")
    tabla_reclusos.pack(fill="both", expand=True, padx=10, pady=10)  # Añadir márgenes alrededor de la tabla

    # Obtener datos de la base de datos y mostrarlos en la tabla
    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Cod_recluso, Nombre, Apellido FROM Recluso")
    resultados = cursor.fetchall()
    conn.close()

    for resultado in resultados:
        codigo = int(resultado[0])
        nombre = resultado[1]
        apellido = resultado[2]
        tabla_reclusos.insert("", "end", values=(codigo, nombre, apellido))

def actualizar_recluso(event=None):
    codigo_recluso = entrada_codigo.get()

    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre, Apellido, Fecha_nacimiento FROM Recluso WHERE Cod_recluso=?", (codigo_recluso,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        entrada_nombre.config(state="normal")
        entrada_nombre.delete(0, "end")
        entrada_nombre.insert(0, resultado[0])
        entrada_nombre.config(state="readonly")

        entrada_apellido.config(state="normal")
        entrada_apellido.delete(0, "end")
        entrada_apellido.insert(0, resultado[1])
        entrada_apellido.config(state="readonly")

        entrada_fecha_nacimiento.config(state="normal")
        entrada_fecha_nacimiento.delete(0, "end")
        entrada_fecha_nacimiento.insert(0, resultado[2])
        entrada_fecha_nacimiento.config(state="readonly")

def guardar_cambios():
    codigo_recluso = entrada_codigo.get()
    nombre = entrada_nombre_editar.get()
    apellido = entrada_apellido_editar.get()
    fecha_nacimiento = entrada_fecha_nacimiento_editar.get()

    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Recluso SET Nombre=?, Apellido=?, Fecha_nacimiento=? WHERE Cod_recluso=?",
        (nombre, apellido, fecha_nacimiento, codigo_recluso),
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Cambios guardados", "Los cambios se han guardado correctamente.")

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Editar Recluso")
ventana.geometry("1200x720")  # Establecer las dimensiones de la ventana

# Dividir la ventana en dos frames
frame_izquierdo = Frame(ventana)
frame_izquierdo.pack(side="left", fill="both", expand=True)

frame_derecho = Frame(ventana)
frame_derecho.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Mostrar la tabla de reclusos
mostrar_reclusos()

# Etiqueta y campo de texto para ingresar el código de recluso
label_codigo = Label(frame_derecho, text="Código de Recluso:", font=("Arial", 12))
label_codigo.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_codigo = Entry(frame_derecho, font=("Arial", 12))
entrada_codigo.pack(pady=(0, 20))

# Etiqueta y campo de texto para mostrar el nombre del recluso
label_nombre = Label(frame_derecho, text="Nombre:", font=("Arial", 12))
label_nombre.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_nombre = Entry(frame_derecho, state="readonly", font=("Arial", 12), width=30)
entrada_nombre.pack(pady=(0, 20))

# Etiqueta y campo de texto para mostrar el apellido del recluso
label_apellido = Label(frame_derecho, text="Apellido:", font=("Arial", 12))
label_apellido.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_apellido = Entry(frame_derecho, state="readonly", font=("Arial", 12), width=30)
entrada_apellido.pack(pady=(0, 20))

# Etiqueta y campo de texto para mostrar la fecha de nacimiento del recluso
label_fecha_nacimiento = Label(frame_derecho, text="Fecha de Nacimiento:", font=("Arial", 12))
label_fecha_nacimiento.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_fecha_nacimiento = Entry(frame_derecho, state="readonly", font=("Arial", 12), width=30)
entrada_fecha_nacimiento.pack(pady=(0, 20))

entrada_codigo.bind("<Return>", actualizar_recluso)

# Etiqueta y campo de texto para editar el nombre del recluso
label_nombre_editar = Label(frame_derecho, text="Editar Nombre:", font=("Arial", 12))
label_nombre_editar.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_nombre_editar = Entry(frame_derecho, font=("Arial", 12), width=30)
entrada_nombre_editar.pack(pady=(0, 20))

# Etiqueta y campo de texto para editar el apellido del recluso
label_apellido_editar = Label(frame_derecho, text="Editar Apellido:", font=("Arial", 12))
label_apellido_editar.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_apellido_editar = Entry(frame_derecho, font=("Arial", 12), width=30)
entrada_apellido_editar.pack(pady=(0, 20))

# Etiqueta y campo de texto para editar la fecha de nacimiento del recluso
label_fecha_nacimiento_editar = Label(frame_derecho, text="Editar Fecha de Nacimiento:", font=("Arial", 12))
label_fecha_nacimiento_editar.pack(pady=(20, 5))  # Ajustar el relleno vertical

entrada_fecha_nacimiento_editar = Entry(frame_derecho, font=("Arial", 12), width=30)
entrada_fecha_nacimiento_editar.pack(pady=(0, 20))

# Botón para guardar los cambios
boton_guardar = Button(frame_derecho, text="Guardar Cambios", font=("Arial", 12), command=guardar_cambios)
boton_guardar.pack(pady=(20, 0))

ventana.mainloop()








