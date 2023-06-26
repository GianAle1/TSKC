from tkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import messagebox
from tkinter import ttk
import pyodbc
from datetime import datetime
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

def get_crimes():
    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Cod_crimen, Nombre FROM Crimen")
    return cursor.fetchall()

def get_celdas():
    conn = pyodbc.connect(
        f"Driver={DB_DRIVER};"
        f"Server={DB_SERVER};"
        f"Database={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT Cod_celda, Numero FROM Celda")
    return cursor.fetchall()

def guardar_datos():
    # Obtener los valores ingresados por el usuario
    nombres = entry_nombres.get()
    apellidos = entry_apellidos.get()
    fecha_nacimiento = entry_fecha_nacimiento.get()
    cod_crimen = cod_crimen_combobox.get()
    cod_celda = cod_celda_combobox.get()

    # Verificar si los campos están vacíos
    if nombres == "" or apellidos == "" or fecha_nacimiento == "" or cod_crimen == "" or cod_celda == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
    else:
        # Inicializar cod_conducta y cod_curso en 0
        cod_conducta = 0
        cod_curso = 0

        # Inicializar peligrosidad y comentario con valores predeterminados
        peligrosidad = 0
        comentario = "Sin comentarios"

        # Guardar los datos en la base de datos
        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )
        cursor = conn.cursor()

        try:
            # Convertir la cadena de fecha al formato adecuado
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()

            # Obtener el siguiente valor para Cod_recluso
            cursor.execute("SELECT MAX(Cod_recluso) FROM Recluso")
            result = cursor.fetchone()
            cod_recluso = result[0] + 1 if result[0] else 1

            # Obtener el código de crimen correspondiente al nombre seleccionado
            cursor.execute("SELECT Cod_crimen FROM Crimen WHERE Nombre=?", cod_crimen)
            cod_crimen = cursor.fetchone()[0]

            # Obtener el código de celda correspondiente al número seleccionado
            cursor.execute("SELECT Cod_celda FROM Celda WHERE Numero=?", cod_celda)
            cod_celda = cursor.fetchone()[0]

            # Insertar el registro en la tabla Recluso
            cursor.execute(
                "INSERT INTO Recluso (Cod_recluso, Nombre, Apellido, Fecha_nacimiento, Cod_crimen, Cod_curso, Cod_conducta, Cod_celda, Peligrosidad, Comentario) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (cod_recluso, nombres, apellidos, fecha_nacimiento, cod_crimen, cod_curso, cod_conducta, cod_celda, peligrosidad, comentario)
            )

            conn.commit()
            messagebox.showinfo("Registro exitoso", "El preso ha sido registrado correctamente.")

            # Limpiar los campos de entrada después de guardar
            entry_nombres.delete(0, END)
            entry_apellidos.delete(0, END)
            entry_fecha_nacimiento.delete(0, END)
            cod_crimen_combobox.set("")
            cod_celda_combobox.set("")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Utilice el formato dd/mm/yyyy.")

        conn.close()

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Registrar Presos")
ventana.geometry("1360x760")

imagen_fondo = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1366, 768), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Cargar la imagen representativa
imagen_registrarpresos = Image.open("Desarrollo/SSPP/Codigo/imagenes/RegistrarPresos.png")
imagen_registrarpresos = imagen_registrarpresos.resize((380, 380), Image.LANCZOS)
imagen_registrarpresos = ImageTk.PhotoImage(imagen_registrarpresos)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0)
logo = Label(ventana, image=imagen_registrarpresos)
logo.place(x=270, y=120)

# Titulo
Titulo = Label(ventana, text="Registrar Preso:", font=("Arial", 20))
Titulo.place(relx=0.6, rely=0.1, anchor="e")

# Campos de texto
label_nombres = Label(ventana, text="Nombres:", font=("Arial", 16))
label_nombres.place(relx=0.6, rely=0.2, anchor="w")
entry_nombres = Entry(ventana, font=("Arial", 16))
entry_nombres.place(relx=0.6, rely=0.24, anchor="w")

label_apellidos = Label(ventana, text="Apellidos:", font=("Arial", 16))
label_apellidos.place(relx=0.6, rely=0.3, anchor="w")
entry_apellidos = Entry(ventana, font=("Arial", 16))
entry_apellidos.place(relx=0.6, rely=0.34, anchor="w")

label_fecha_nacimiento = Label(ventana, text="Fecha de Nacimiento:", font=("Arial", 16))
label_fecha_nacimiento.place(relx=0.6, rely=0.4, anchor="w")
entry_fecha_nacimiento = Entry(ventana, font=("Arial", 16))
entry_fecha_nacimiento.place(relx=0.6, rely=0.44, anchor="w")

label_cod_crimen = Label(ventana, text="Crimen:", font=("Arial", 16))
label_cod_crimen.place(relx=0.6, rely=0.5, anchor="w")
cod_crimen_combobox = ttk.Combobox(ventana, values=[row[1] for row in get_crimes()], font=("Arial", 16))
cod_crimen_combobox.place(relx=0.6, rely=0.54, anchor="w")

label_cod_celda = Label(ventana, text="Celda:", font=("Arial", 16))
label_cod_celda.place(relx=0.6, rely=0.6, anchor="w")
cod_celda_combobox = ttk.Combobox(ventana, values=[row[1] for row in get_celdas()], font=("Arial", 16))
cod_celda_combobox.place(relx=0.6, rely=0.64, anchor="w")

# Botón Guardar
boton_guardar = Button(ventana, text="Guardar", command=guardar_datos, font=("Arial", 18))
boton_guardar.place(relx=0.5, rely=0.75, anchor=CENTER)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

