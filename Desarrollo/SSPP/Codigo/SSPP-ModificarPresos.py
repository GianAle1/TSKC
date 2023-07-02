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
imagen_fondo = imagen_fondo.resize((1360, 760), Image.LANCZOS)
imagen_fondo = imagen_fondo.filter(ImageFilter.BLUR)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

# Mostrar la imagen de fondo en un widget Label
fondo = Label(ventana, image=imagen_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Cargar la imagen de ModificarPresos
imagen_lateral = Image.open("imagenes\ModificarPreso.png")
imagen_lateral = imagen_lateral.resize((470, 400), Image.LANCZOS)
imagen_lateral = ImageTk.PhotoImage(imagen_lateral)

# Mostrar la imagen Modificar Presos
label_imagen_lateral = Label(ventana, image=imagen_lateral)
label_imagen_lateral.place(x=500, y=100)

# Crear un contenedor Frame para la imagen y el título
frame_lateral = Frame(ventana)
frame_lateral.place(x=500, y=100)

# Mostrar la imagen lateral en un widget Label
label_imagen_lateral = Label(frame_lateral, image=imagen_lateral)
label_imagen_lateral.pack()

# Mostrar el título "Modificar Presos" en un widget Label
titulo = Label(frame_lateral, text="Modificar Perfil de Presos", font=("Arial", 16))
titulo.pack()

# Botón "Atrás"
boton_atras = Button(ventana, text="Atrás", font=("Arial", 16), command=cerrar_ventana)
boton_atras.place(x=1200, y=20, width=100, height=40)

# Botón "Editar Información"
boton_editar_info = Button(ventana, text="Editar Información", font=("Arial", 16), command=editar_preso)
boton_editar_info.place(x=200, y=150, width=200, height=50)

# Botón "Talleres"
boton_talleres = Button(ventana, text="Talleres", font=("Arial", 16), command=editar_taller)
boton_talleres.place(x=200, y=250, width=200, height=50)

# Botón "Perfil Psicológico"
boton_perfil_psico = Button(ventana, text="Perfil Psicológico", font=("Arial", 16), command=perfil_psicologico)
boton_perfil_psico.place(x=200, y=350, width=200, height=50)

# Botón "Comentarios"
boton_comentarios = Button(ventana, text="Comentarios", font=("Arial", 16), command=agregar_comentario)
boton_comentarios.place(x=200, y=450, width=200, height=50)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()