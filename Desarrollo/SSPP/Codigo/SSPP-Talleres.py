from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

# Función para mostrar los talleres seleccionados
def mostrar_taller():
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

    # Etiqueta y campo de texto para ingresar el código de recluso
    label_codigo = Label(frame_derecho, text="Código de Recluso:", font=("Arial", 12))
    label_codigo.pack(pady=(200, 5))  # Ajustar el relleno vertical

    entrada_codigo = Entry(frame_derecho, font=("Arial", 12))
    entrada_codigo.pack(pady=(0, 20))

    # Etiqueta y campo de texto para mostrar el nombre del recluso
    label_recluso = Label(frame_derecho, text="Nombre:", font=("Arial", 12))
    label_recluso.pack(pady=(20, 5))  # Ajustar el relleno vertical

    entrada_recluso = Entry(frame_derecho, state="readonly", font=("Arial", 12), width=30)
    entrada_recluso.pack(pady=(0, 20))

    # Etiqueta y campo de texto para mostrar el apellido del recluso
    label_apellido = Label(frame_derecho, text="Apellido:", font=("Arial", 12))
    label_apellido.pack(pady=(20, 5))  # Ajustar el relleno vertical

    entrada_apellido = Entry(frame_derecho, state="readonly", font=("Arial", 12), width=30)
    entrada_apellido.pack(pady=(0, 20))

    # Etiqueta y combobox para seleccionar el taller
    label_taller = Label(frame_derecho, text="Ingrese taller:", font=("Arial", 12))
    label_taller.pack(pady=(20, 5))  # Ajustar el relleno vertical

    combobox_taller = ttk.Combobox(frame_derecho, state="readonly", font=("Arial", 12))
    combobox_taller.pack(pady=(0, 20))

    # Obtener los nombres de los talleres y mostrarlos en el combobox
    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Curso")
    nombres_talleres = [row[0] for row in cursor.fetchall()]
    conn.close()

    combobox_taller["values"] = nombres_talleres

    def actualizar_recluso(event=None):
        codigo = entrada_codigo.get()

        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT Nombre, Apellido FROM Recluso WHERE Cod_recluso=?", (codigo,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            entrada_recluso.config(state="normal")
            entrada_recluso.delete(0, "end")
            entrada_recluso.insert(0, resultado[0])
            entrada_recluso.config(state="readonly")

            entrada_apellido.config(state="normal")
            entrada_apellido.delete(0, "end")
            entrada_apellido.insert(0, resultado[1])
            entrada_apellido.config(state="readonly")

    entrada_codigo.bind("<Return>", actualizar_recluso)

    def guardar_taller():
        codigo = entrada_codigo.get()
        nombre_taller = combobox_taller.get()

        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )
        cursor = conn.cursor()
        
        # Obtener el código del taller basado en su nombre
        cursor.execute("SELECT Cod_curso FROM Curso WHERE Nombre=?", (nombre_taller,))
        resultado = cursor.fetchone()
        if resultado:
            codigo_taller = resultado[0]

            # Actualizar el código del taller para el recluso en la tabla Recluso
            cursor.execute("UPDATE Recluso SET Cod_curso=? WHERE Cod_recluso=?", (codigo_taller, codigo))
            conn.commit()
            conn.close()

            messagebox.showinfo("Taller actualizado", "El taller se ha actualizado correctamente.")
        else:
            messagebox.showwarning("Taller no encontrado", "El taller seleccionado no existe.")

    boton_guardar_taller = Button(frame_derecho, text="Guardar Taller", command=guardar_taller, font=("Arial", 12))
    boton_guardar_taller.pack(pady=20)  # Ajustar el relleno vertical

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Modificar Talleres")
ventana.geometry("1360x760")

# Creación de los marcos
frame_izquierdo = Frame(ventana, width=600, height=720)
frame_derecho = Frame(ventana, width=600, height=720)

# Anclaje de los marcos a la izquierda y derecha de la ventana
frame_izquierdo.pack(side="left", fill="both", expand=True)
frame_derecho.pack(side="right", fill="both", expand=True)

# Llamar a la función para mostrar los talleres
mostrar_taller()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()












