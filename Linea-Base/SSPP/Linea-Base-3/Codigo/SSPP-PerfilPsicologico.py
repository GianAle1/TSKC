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

    # Etiqueta y combobox para seleccionar la conducta
    label_conducta = Label(frame_derecho, text="Conducta:", font=("Arial", 12))
    label_conducta.pack(pady=(20, 5))  # Ajustar el relleno vertical

    combobox_conducta = ttk.Combobox(frame_derecho, state="readonly", font=("Arial", 12))
    combobox_conducta.pack(pady=(0, 20))

    # Obtener los nombres de conducta y mostrarlos en el combobox
    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Nombre FROM Conducta")
    nombres_conducta = [row[0] for row in cursor.fetchall()]
    conn.close()

    combobox_conducta["values"] = nombres_conducta

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

    def guardar_perfil_psicologico():
        codigo = entrada_codigo.get()
        nombre_conducta = combobox_conducta.get()
        peligrosidad = entrada_peligrosidad.get()

        if not peligrosidad.isdigit():
            messagebox.showerror("Error", "La peligrosidad debe ser un valor numérico.")
            return

        peligrosidad = int(peligrosidad)
        if peligrosidad < 1 or peligrosidad > 10:
            messagebox.showerror("Error", "La peligrosidad debe estar en el rango de 1 a 10.")
            return

        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )
        cursor = conn.cursor()

        # Obtener el código de conducta basado en su nombre
        cursor.execute("SELECT Cod_conducta FROM Conducta WHERE Nombre=?", (nombre_conducta,))
        resultado = cursor.fetchone()
        if resultado:
            codigo_conducta = resultado[0]

            # Actualizar el código de conducta y la peligrosidad para el recluso en la tabla Recluso
            cursor.execute("UPDATE Recluso SET Cod_conducta=?, Peligrosidad=? WHERE Cod_recluso=?", (codigo_conducta, peligrosidad, codigo))
            conn.commit()
            conn.close()

            messagebox.showinfo("Perfil Psicológico actualizado", "El perfil psicológico se ha actualizado correctamente.")
        else:
            messagebox.showwarning("Conducta no encontrada", "La conducta seleccionada no existe.")

    # Etiqueta y campo de texto para ingresar la peligrosidad
    label_peligrosidad = Label(frame_derecho, text="Peligrosidad:", font=("Arial", 12))
    label_peligrosidad.pack(pady=(20, 5))  # Ajustar el relleno vertical

    entrada_peligrosidad = Entry(frame_derecho, font=("Arial", 12), width=30)
    entrada_peligrosidad.pack(pady=(0, 20))

    boton_guardar = Button(frame_derecho, text="Guardar", font=("Arial", 12), command=guardar_perfil_psicologico)
    boton_guardar.pack()

    ventana.mainloop()


# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Modificar Perfil Psicológico")
ventana.geometry("1200x720")  # Establecer las dimensiones de la ventana

# Dividir la ventana en dos frames
frame_izquierdo = Frame(ventana)
frame_izquierdo.pack(side="left", fill="both", expand=True)

frame_derecho = Frame(ventana)
frame_derecho.pack(side="right", fill="both", expand=True)

mostrar_taller()

