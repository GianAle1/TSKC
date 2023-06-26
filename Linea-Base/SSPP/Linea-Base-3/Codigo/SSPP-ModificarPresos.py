from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import subprocess

def cerrar_ventana():
    ventana.destroy()

def editar_preso():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-EditarPresos.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def editar_taller():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-Talleres.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def perfil_psicologico():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-PerfilPsicologico.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

def agregar_comentario():
    ventana.withdraw()  # Oculta la ventana actual
    subprocess.call(["python", "SSPP-Comentarios.py"])
    ventana.deiconify()  # Muestra la ventana principal nuevamente

# Crear la ventana principal
ventana = Tk()
ventana.title("SSPP - Modificar Presos")
ventana.geometry("1360x760")

# Cargar la imagen de fondo
imagen_fondo = Image.open("imagenes\puertaCelda.jpg")
imagen_fondo = imagen_fondo.resize((1200, 720), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1200, y=20, width=100, height=40)

# Botón "Editar Información"
boton_editar_info = Button(ventana, text="Editar Información", font=("Arial", 16), command=editar_preso)
boton_editar_info.place(x=100, y=100, width=200, height=50)

# Botón "Talleres"
boton_talleres = Button(ventana, text="Talleres", font=("Arial", 16), command=editar_taller)
boton_talleres.place(x=100, y=200, width=200, height=50)

# Botón "Perfil Psicológico"
boton_perfil_psico = Button(ventana, text="Perfil Psicológico", font=("Arial", 16), command=perfil_psicologico)
boton_perfil_psico.place(x=100, y=300, width=200, height=50)

# Botón "Comentarios"
boton_comentarios = Button(ventana, text="Comentarios", font=("Arial", 16), command=agregar_comentario)
boton_comentarios.place(x=100, y=400, width=200, height=50)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()