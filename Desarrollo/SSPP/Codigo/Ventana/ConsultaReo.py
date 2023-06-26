from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

from Clase.Crimen import *
from Clase.Reo import *
from PIL import ImageTk, Image
class Ventana(Frame):
    reo = Reo()

    def __init__(self, master=None):
        super().__init__(master, width=1920, height=1080)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()

    def llenaDatos(self):
        datos = self.reo.consulta_preso()
        for row in datos:
            self.grid.insert("", END, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    def fNuevo(self):
        pass

    def fGuardar(self):
        self.reo.inserta_preso(self.txtNombre.get(), self.txtApellido.get(), self.txtCrimen.get())
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        # Agregar imagen de fondo
        

        """# Cuadro azul
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=400)
        self.btnNuevo = Button(frame1, text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)
        self.btnModificar = Button(frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)
        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        # Cuadro verde
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95, y=0, width=200, height=400)
        lbl2 = Label(frame2, text="Nombre")
        lbl2.place(x=3, y=55)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=3, y=75, width=100, height=20)
        lbl3 = Label(frame2, text="Apellido: ")
        lbl3.place(x=3, y=105)
        self.txtApellido = Entry(frame2)
        self.txtApellido.place(x=3, y=125, width=100, height=20)

        lbl1 = Label(frame2, text="Fecha de nacimiento: ")
        lbl1.place(x=3, y=155)
        cal = DateEntry(frame2, width=30, year=2021)
        cal.place(x=3, y=180, width=100, height=30)
        cal.config(headersbackground='#364c55', foreground='#000', background='#fff', headersforeground='#fff')

        lbl4 = Label(frame2, text="Crimen:")
        lbl4.place(x=3, y=215)
        self.cbcrimen = ttk.Combobox(frame2, width=20)
        self.cbcrimen.place(x=3, y=200, width=100, height=30)

        self.txtCrimen = Entry(frame2)
        self.txtCrimen.place(x=3, y=240, width=100, height=20)

        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=300, width=60, height=30)
        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80, y=300, width=60, height=30)

        self.cbnivelConducta = ttk.Combobox(frame2, width=20)
        self.cbnivelConducta.place(x=3, y=275, width=100, height=30)
        opciones = ['Alto', 'Medio', 'Bajo']
        self.cbnivelConducta.set("No calificado")
        self.cbnivelConducta['values'] = opciones"""

        self.grid = ttk.Treeview(self, columns=("col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.grid.column("#0", width=1)
        self.grid.column("col0", width=120)
        self.grid.column("col1", width=120)
        self.grid.column("col2", width=120)
        self.grid.column("col3", width=120)
        self.grid.column("col4", width=120)
        self.grid.column("col5", width=120)
        self.grid.column("col6", width=120)
        self.grid.heading("col0", text="Nombre", anchor=CENTER)
        self.grid.heading("col1", text="Apellido", anchor=CENTER)
        self.grid.heading("col2", text="Fecha de nacimiento", anchor=CENTER)
        self.grid.heading("col3", text="Crimen", anchor=CENTER)
        self.grid.heading("col4", text="Numero de celda", anchor=CENTER)
        self.grid.heading("col5", text="Prision", anchor=CENTER)
        self.grid.heading("col6", text="Curso", anchor=CENTER)
        self.grid.heading("col7", text="Conducta", anchor=CENTER)
        self.grid.place(x=247, y=0, width=1100, height=750)