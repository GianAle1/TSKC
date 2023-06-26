import pyodbc
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageFilter
import subprocess
from ConfigurarConexionBD import DB_DRIVER, DB_SERVER, DB_DATABASE, DB_USERNAME, DB_PASSWORD

imagen_fondo_registro = None
fondo_registro = None

def iniciar_sesion():
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showerror("Error", "Por favor, ingresa un usuario y una contraseña.")
    else:
         # Establecer la conexión con SQL Server
        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )    
        
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM Clientes WHERE Usuario=? AND Contraseña=?", (usuario, contrasena))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
            abrir_archivo()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def guardar_registro():
    usuario = entrada_usuario_registro.get()
    contrasena = entrada_contrasena_registro.get()
    empresa = entrada_empresa_registro.get()

    if not usuario or not contrasena or not empresa:
        messagebox.showerror("Error", "Por favor, ingresa un usuario, una contraseña y el nombre de la empresa.")
    else:
        conn = pyodbc.connect(
            f"Driver={DB_DRIVER};"
            f"Server={DB_SERVER};"
            f"Database={DB_DATABASE};"
            f"UID={DB_USERNAME};"
            f"PWD={DB_PASSWORD};"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Clientes WHERE Usuario=?", (usuario,))
        if cursor.fetchone():
            messagebox.showerror("Error", "El usuario ya existe. Por favor, elige otro nombre de usuario.")
        else:
            cursor.execute("INSERT INTO Clientes (Usuario, Contraseña, Empresa) VALUES (?, ?, ?)", (usuario, contrasena, empresa))
            conn.commit()
            messagebox.showinfo("Registro exitoso", "El usuario se registró correctamente.")
            ventana_registro.destroy()


def regresar():
    ventana_registro.destroy()

def registrar():
    global ventana_registro, entrada_usuario_registro, entrada_contrasena_registro, entrada_empresa_registro, imagen_fondo_registro
    global imagen_fondo_registro, fondo_registro
    ventana_registro = Toplevel(ventana)
    ventana_registro.title("SSPP-Registrar Presos")
    ventana_registro.geometry("800x600")

    imagen_fondo_registro = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
    imagen_fondo_registro = imagen_fondo_registro.resize((800, 600), Image.LANCZOS)
    imagen_fondo_registro = imagen_fondo_registro.filter(ImageFilter.BLUR)
    fondo_registro = ImageTk.PhotoImage(imagen_fondo_registro)

    label_fondo_registro = Label(ventana_registro, image=fondo_registro)
    label_fondo_registro.place(x=0, y=0, relwidth=1, relheight=1)

    ancho_ventana_registro = 800
    ancho_entrada = 400
    x_entrada = (ancho_ventana_registro - ancho_entrada) // 2

    label_empresa_registro = Label(ventana_registro, text="Empresa:", font=("Arial", 14))
    label_empresa_registro.place(x=x_entrada, y=150)

    entrada_empresa_registro = Entry(ventana_registro, width=30, font=("Arial", 14))
    entrada_empresa_registro.place(x=x_entrada, y=180)

    label_usuario_registro = Label(ventana_registro, text="Usuario:", font=("Arial", 14))
    label_usuario_registro.place(x=x_entrada, y=220)

    entrada_usuario_registro = Entry(ventana_registro, width=30, font=("Arial", 14))
    entrada_usuario_registro.place(x=x_entrada, y=250)

    label_contrasena_registro = Label(ventana_registro, text="Contraseña:", font=("Arial", 14))
    label_contrasena_registro.place(x=x_entrada, y=290)

    entrada_contrasena_registro = Entry(ventana_registro, show="*", width=30, font=("Arial", 14))
    entrada_contrasena_registro.place(x=x_entrada, y=320)

    x_boton = x_entrada + 80
    y_boton = 380

    boton_guardar_registro = Button(ventana_registro, text="Guardar", command=guardar_registro, font=("Arial", 14))
    boton_guardar_registro.place(x=x_boton, y=y_boton)

    boton_atras = Button(ventana_registro, text="Atrás", command=regresar, font=("Arial", 14))
    boton_atras.place(x=x_boton + 100, y=y_boton)

def abrir_archivo():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-Inicio.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Login")
ventana.geometry("1360x760")

# Cargar la imagen de fondo
imagen_fondo = Image.open("Desarrollo/SSPP/Codigo/imagenes/puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1360, 760), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de lienzo para la imagen de fondo
canvas = Canvas(ventana, width=1200, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fondo, anchor="nw")

# Etiqueta de usuario
label_usuario = Label(ventana, text="Usuario:", font=("Arial", 16, "bold"), anchor="w", justify="left")
label_usuario.place(x=500, y=180, relwidth=0.3)

# Campo de entrada de usuario
entrada_usuario = Entry(ventana, font=("Arial", 16))
entrada_usuario.place(x=500, y=210, relwidth=0.3)

# Etiqueta de contraseña
label_contrasena = Label(ventana, text="Contraseña:", font=("Arial", 16, "bold"), anchor="w", justify="right")
label_contrasena.place(x=500, y=260, relwidth=0.3)

# Campo de entrada de contraseña
entrada_contrasena = Entry(ventana, show="*", font=("Arial", 16))
entrada_contrasena.place(x=500, y=290, relwidth=0.3)

# Botón de inicio de sesión
boton_iniciar_sesion = Button(ventana, text="Iniciar Sesión", command=iniciar_sesion, font=("Arial", 16, "bold"))
boton_iniciar_sesion.place(x=500, y=360, relwidth=0.3)

# Botón de registrar
boton_registrar = Button(ventana, text="Registrar", command=registrar, font=("Arial", 16, "bold"))
boton_registrar.place(x=500, y=410, relwidth=0.3)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()